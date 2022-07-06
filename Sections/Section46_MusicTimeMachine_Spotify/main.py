import os,re

from bs4 import BeautifulSoup
import requests

import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

from Config import Config

config = Config()

DIR = os.path.dirname(os.path.realpath(__file__))

# SCC = SpotifyClientCredentials(
#     client_id= config.data['CLIENT_ID']
#     ,client_secret=config.data['CLIENT_SECRET']
#     #,
#     # scope="playlist-modify-private"
#     # ,redirect_uri="http://example.com"
#     # ,show_dialog=True
#     # ,cache_path= os.path.join(DIR, "token.txt")
#     # ,cache_path= "token.txt"
#     )

SCC = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id= config.data['CLIENT_ID']
        ,client_secret=config.data['CLIENT_SECRET']))

SOA = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= config.data['CLIENT_ID']
    ,client_secret=config.data['CLIENT_SECRET']
    ,scope="playlist-modify-private"
    ,redirect_uri="https://example.com/JGarza9788"
    ,show_dialog=True
    # ,cache_path= os.path.join(DIR, "token.txt"))
    # ,cache_path= "token.txt")
    ))

# sp=spotipy.Spotify(
# auth_manager=SpotifyOAuth(
# scope="playlist-modify-private",
# redirect_uri="https://example.com/JGarza9788",
# client_id= config.data['CLIENT_ID'],
# client_secret=config.data['CLIENT_SECRET'],
# show_dialog=True,
# cache_path="token.txt"
# )
# )

def ask_for_date():
    '''
    '''
    done = False
    while done == False:
        i = input("Which year do you want to travel to? (enter in YYYY-MM-DD format)\n")
        if re.match(r'\d\d\d\d-\d\d-\d\d',i):
            done = True
            return i
        else:
            print("the date should be in YYYY-MM-DD format\n")
            done = False

def get_song_uris(list_of_songs,date):
    song_uris = []
    year = date.split("-")[0]
    for index,song in enumerate(list_of_songs):
        # print(index,len(list_of_songs))
        p = index/len(list_of_songs)
        print("{:.2f}".format( p * 100),"[" + ("#"*int(p*50)).ljust(50," ") + "]")

        try:
            result = SCC.search(q=f"track:{song} year:{year}", type="track") #, market="ES", limit=1)
        # print(result)

            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            pass
            # print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris

def main():
    date = ask_for_date()
    print("\n\nhold on!\n we are going to  ... " + date)

    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_div = soup.find_all("div", class_="o-chart-results-list-row-container")

    song_names = []
    for index,div in  enumerate(song_names_div):

        p = index/len(song_names_div)
        print("{:.2f}".format( p * 100),"[" + ("#"*int(p*50)).ljust(50," ") + "]")

        sn = div.find_all("h3",id="title-of-a-story")[0].getText().strip().replace('\t','')
        print(index,sn)
        song_names.append(sn)

    s_uri = get_song_uris(song_names,date)
    print(*s_uri,sep='\n')

    #Creating a new private playlist in Spotify
    playlist = SOA.user_playlist_create(user=config.data["user_id"], name=f"{date} Billboard 100", public=False)
    print(playlist)

    #Adding songs found into the new playlist
    SOA.playlist_add_items(playlist_id=playlist["id"], items=s_uri)

    

if __name__ == '__main__':

    main()
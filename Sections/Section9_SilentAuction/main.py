
import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

from art import logo
from clear_screen import clear

def get_bid(e):
    # print(e)
    try:
        return e['bid']
    except:
        return 0.0 

def main():

    # clear bids
    bids = []
    more_bids = True
    bidmap = {'Yes':True,'No':False}

    while more_bids:
        
        name = pyask.ask_question('What is your name? ',str)
        bid = pyask.ask_question('What is your Bid? ',float)

        bids.append({'name':name,'bid':bid})
        more_bids = bidmap[pyask.choose_one(['No','Yes'],text='Are there any other bidders? ')]
        clear()

    bids.sort(key=get_bid,reverse=True)
    # print(*bids,sep='\n')

    print('The Winner is {0}, with a bid of ${1}!'.format(bids[0]['name'],bids[0]['bid']))



if __name__ == "__main__":
    main()

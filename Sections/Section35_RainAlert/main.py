
# rain on pythonanywhere.com


from weather_to_nerdfont import get_nf_icon # to get cool weather icons
import requests
from twilio.rest import Client

def get_weather_data():
    # url = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    # url = url.format(city_name='Charlotte,NC',API_key='e8f4614b22e6f00f4a4d1c7554f77ab7')

    # url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}'
    # url = url.format(lat=35.237928,lon=-80.859074,part="daily",API_key="e8f4614b22e6f00f4a4d1c7554f77ab7")

    # url = 'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={API_key}'
    # url = url.format(zip_code="28202",country_code="US",API_key="e8f4614b22e6f00f4a4d1c7554f77ab7")

    # url = 'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API_key}'
    # url = url.format(lat=35.237928,lon=-80.859074,limit=1,API_key="e8f4614b22e6f00f4a4d1c7554f77ab7")

    # url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
    # url = url.format(lat=35.237928,lon=-80.859074,API_key="e8f4614b22e6f00f4a4d1c7554f77ab7")

    url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}'
    url = url.format(lat=35.237928,lon=-80.859074,API_key="e8f4614b22e6f00f4a4d1c7554f77ab7")

    # print(url)

    response = requests.get(url)
    # print(response.status_code)
    response.raise_for_status()
    # print(response.json())

    return response.json()

def get_message(data=None,three_hour_times = 8):

    if data == None:
        data = get_weather_data()

    message = ''
    for i in range(three_hour_times):
        w = data['list'][i]['weather'][0]
        # print(w['id'])
        msg = '{0} - {1} {2}\n'
        msg = msg.format(data['list'][i]['dt_txt'].split(' ')[1],get_nf_icon(w['id']),w['description'])

        message += msg

    return message

def will_rain(data = None,three_hour_times = 8):

    if data == None:
        data = get_weather_data()
    d = data['list'][:three_hour_times]
    
    result = False

    for i in d:
        # print(i['weather'][0]['id'])
        if i['weather'][0]['id'] >= 300 and i['weather'][0]['id'] <= 599:
            result = True
            break;
    return result

def get_umbrella(data=None,three_hour_times = 8):
    if data == None:
        data = get_weather_data()

    if will_rain(data,three_hour_times):
        return 'get the umbrella ☂'
    else:
        return ''

def main():
    account = "AC34aac68cc548899af9859e92cd7f38f8"
    token = "2a9d15b051279e15dc7421ddf6723338"
    client = Client(account, token)

    data = get_weather_data()
    three_hour_times = 9

    # print(get_message(data,three_hour_times))
    # print(will_rain(data,three_hour_times))
    # print(get_umbrella(data,three_hour_times))

    if will_rain(data,three_hour_times):
        message = client.messages.create(  
                              messaging_service_sid='MG2e4b80d6d35dd0dfbecbc707b4f429fa', 
                              body=get_umbrella(data,three_hour_times),      
                              to='+18182510647' 
                          ) 
        


if __name__ == '__main__':
    # data = get_weather_data()
    # print(get_message(data))
    # print(will_rain(data))
    # print(get_umbrella(data))

    main()
import os,json
from datetime import datetime
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.


    
    def __init__(self,config_data):
        self.data = {}

        # self.sheet_endpoint = "https://api.sheety.co/a66265942c4341dc164e0bd22797f82a/flightDeals/prices"

        self.sheet_prices = "https://api.sheety.co/a66265942c4341dc164e0bd22797f82a/flightDeals/prices"
        self.sheet_users = "https://api.sheety.co/a66265942c4341dc164e0bd22797f82a/flightDeals/users"

        self.headers = {
            "Authorization": f"Bearer {config_data['SHEETY']['API_KEY']}"
        }

    def get_destination_data(self):
        response = requests.get(
            self.sheet_prices,
            headers=self.headers,
        )
        self.status_code = response.status_code
        self.data = response.json()['prices']

        return self.data

    def set_data(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheet_prices}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            self.sheet_users,
            headers=self.headers,
        )
        self.status_code = response.status_code
        self.data = response.json()['users']

        return self.data

if __name__ == "__main__":
    from Config import Config
    config = Config()
    DM = DataManager(config.data)
    print(DM.get_customer_emails())
    


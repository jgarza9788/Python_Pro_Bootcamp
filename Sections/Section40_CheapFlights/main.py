#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os,json
from datetime import datetime, timedelta

from Config import Config
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

config = Config()


ORIGIN_CITY_IATA = "LON"


data_manager = DataManager(config.data)
flight_search = FlightSearch(config.data)
notification_manager = NotificationManager(config.data)


sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes(codes)
    sheet_data = data_manager.get_destination_data()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)


# ideally we would want to only have one message that contains a list of the deals on flights


for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

    if flight is None:
        continue;

    if flight.price < destination["lowestPrice"]:

        # notification_manager.send_sms(
        #     message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # )

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        phones = [row["phone"] for row in users]
        message = f"Low price alert! Only {flight.price}USD to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # if flight.stop_overs > 0:
            # message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        # email will not work because google and Yahoo placed restrictions,
        # --> if this was a production application we could use a real service or do everything via selenium
        # notification_manager.send_emails(emails, message, link)

        print(*phones,sep='\n')

        notification_manager.create_sms_spam(
            # names=names,
            phones=phones,
            message=message + '\n' + link
        )
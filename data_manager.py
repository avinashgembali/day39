import os
import requests

username = os.environ.get('USERNAME')
sheety_end_point = f"https://api.sheety.co/{username}/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_end_point)
        data = response.json()["prices"]
        return data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_end_point}/{city['id']}",
                json=new_data
            )
            print(response.text)
import requests
from user_data import UserData
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/b2ca05299dd2ec4560fe1c281941830c/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/b2ca05299dd2ec4560fe1c281941830c/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.users_data ={}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_user_data(self, user_info):
        new_user = {
            "user": {
                "firstName": user_info.first_name,
                "lastName": user_info.last_name,
                "email": user_info.email
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_user)
        response.raise_for_status()

    def get_users_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.users_data = data['users']
        return self.users_data

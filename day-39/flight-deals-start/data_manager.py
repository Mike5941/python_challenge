import requests
from user_data import UserData

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/83303124c232ca252eeb6ba9741c7fc4/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/83303124c232ca252eeb6ba9741c7fc4/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}

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


    def update_user_data(self, user_data: UserData):
        new_user = {
            "user": {
                "firstName": user_data.first_name,
                "lastName": user_data.last_name,
                "email": user_data.email
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_user)
        response.raise_for_status()

    def get_user_data(self):


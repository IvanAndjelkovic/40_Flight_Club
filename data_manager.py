import os
import requests
from dotenv import load_dotenv

load_dotenv()

# The endpoint should look like this: https://api.sheety.co/YOUR_USER_ID/YOUR_PROJECT_NAME/YOUR_SHEET_NAME
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/b18649a7a31a35849e7fc91350c4f2fd/flightDeals/prices"
SHEETY_CUSTOMER_ENDPOINT = "https://api.sheety.co/b18649a7a31a35849e7fc91350c4f2fd/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._password = os.environ["SHEETY_PASSWORD"]
        self._headers = {"Authorization": f"Bearer {self._password.replace('Bearer ', '')}"}
        self.destination_data = {}

    def get_destination_data(self):
        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._headers)
            response.raise_for_status()
            data = response.json()
            print(f"Response status: {response.status_code}")
            print(f"Response data: {data}")
            self.destination_data = data["prices"]
            return self.destination_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []
        
    def get_customer_emails(self):
        try:
            response = requests.get(url=SHEETY_CUSTOMER_ENDPOINT,headers=self._headers)
            response.raise_for_status()
            data = response.json()
            print(f"Response status: {response.status_code}")
            print(f"Response data:  {data}")
            self.customer_data = data
            return self.customer_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        # for city in self.destination_data:
        #     new_data = {
        #         "price": {
        #             "iataCode": city["iataCode"]
        #         }
        #     }
        #     response = requests.put(
        #         url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
        #         json=new_data,
        #         headers=self._headers
        #     )
        #     print(response.text)
        pass
import requests
import os
from dotenv import load_dotenv
import datetime as dt
from pprint import pprint
load_dotenv()
class FlightSearch:
    def __init__(self):
        self.endpoint="https://test.api.amadeus.com/v1/reference-data/locations"
        self.api_key=os.environ.get("API_KEY")
        self.api_secret=os.environ.get("API_Secret")
        self._token=self._get_new_token()
        self.headers={
            "Authorization": f"Bearer {self._token}"
        }

    def get_destinition_code(self, city_name):
        self.config = {
            "subType" : "CITY",
            "keyword" : city_name,
            "page[limit]" : 1
        }
        response = requests.get(url=self.endpoint, headers=self.headers, params=self.config)
        return response.json()["data"][0]["iataCode"]

    def _get_new_token(self):
        self_endpoint_token="https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=self_endpoint_token, headers=header, data=body)
        response.raise_for_status()
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_lowest_price(self, iata_code : str):
        endpoint_lowest = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        date_today= dt.datetime.now() + dt.timedelta(days=1)
        date_after_six_months = dt.datetime.now() + dt.timedelta(days=180)
        parameters = {
            "originLocationCode" : "LON",
            "destinationLocationCode" : iata_code,
            "departureDate" : date_today.strftime("%Y-%m-%d"),
            "returnDate" : date_after_six_months.strftime("%Y-%m-%d"),
            "adults" : "1",
            "nonStop" : "true",
            "currencyCode": "GBP",
            "max": "1"
        }
        response_lowest=requests.get(url=endpoint_lowest, params=parameters, headers=self.headers)
        data = response_lowest.json()
        if "data" in data and len(data["data"]) >0:
            return data["data"][0]
        else:
            print(f"No flights found for {iata_code}")
            return None

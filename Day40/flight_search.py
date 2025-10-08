import requests
import os
from dotenv import load_dotenv
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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        endpoint_lowest = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        parameters = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": "1",
            "nonStop": str(is_direct).lower(),
            "currencyCode": "GBP",
            "max": "1"
        }
        response_lowest = requests.get(url=endpoint_lowest, params=parameters, headers=self.headers)
        data = response_lowest.json()
        if "data" in data and len(data["data"]) > 0:
            segments = data["data"][0]["itineraries"][0]["segments"]
            stops = len(segments) - 1
            final_airport = segments[-1]["arrival"]["iataCode"]
            via_city = segments[0]["arrival"]["iataCode"] if stops > 0 else None
            return {
                "price": data["data"][0]["price"]["total"],
                "stops": stops,
                "final_airport": final_airport,
                "via_city": via_city,
                "departure": segments[0]["departure"]["at"],
                "return_date": data["data"][0]["itineraries"][1]["segments"][0]["arrival"]["at"]
            }
        elif "data" in data and len(data["data"]) == 0:
            parameters["nonStop"] = "false"
            response_lowest = requests.get(url=endpoint_lowest, params=parameters, headers=self.headers)
            data = response_lowest.json()
            if "data" in data and len(data["data"]) > 0:
                segments = data["data"][0]["itineraries"][0]["segments"]
                stops = len(segments) - 1
                final_airport = segments[-1]["arrival"]["iataCode"]
                via_city = segments[0]["arrival"]["iataCode"] if stops > 0 else None
                return {
                    "price": data["data"][0]["price"]["total"],
                    "stops": stops,
                    "final_airport": final_airport,
                    "via_city": via_city,
                    "departure": segments[0]["departure"]["at"],
                    "return_date": data["data"][0]["itineraries"][1]["segments"][0]["arrival"]["at"]
                }
            else:
                print(f"No flights with escale found for {destination_city_code}")
                return None
        else:
            print(f"No flights found for {destination_city_code}")
            return None


import requests
import os
from dotenv import load_dotenv
load_dotenv()


class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/124d4e4694c87649d93898724330b6c0/flightDealsSorin/prices"
        self.headers = {
            "Authorization" : os.environ.get("KEY_SHEETY")
        }

    def read_row(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def update_row(self, row_id: int, iata_cote: str):
        config_update_row = {
            "price": {
                "iataCode": iata_cote
            }
        }
        response_update = requests.put(url=f"{self.endpoint}/{row_id}", json=config_update_row, headers=self.headers)

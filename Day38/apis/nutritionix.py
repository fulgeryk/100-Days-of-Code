import requests
import os
from dotenv import load_dotenv
load_dotenv()

class Nutritionix:
    def __init__(self):
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.headers = {
            "x-app-id" : os.environ.get("APP_ID"),
            "x-app-key" : os.environ.get("APP_KEYS_NUTRITIONIX")
        }
    def get_exercise_stats(self, query: str, user_data: dict):
        nutrixion_config = {
            "query" : query,
            **user_data
        }
        response = requests.post(url=self.endpoint, json=nutrixion_config, headers=self.headers)
        data = response.json()
        return data




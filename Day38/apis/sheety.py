import requests
import os
from dotenv import load_dotenv
load_dotenv()

class Sheety:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/124d4e4694c87649d93898724330b6c0/workoutTracking/workouts"
        self.headers = {
            "Authorization" :f"Bearer {os.environ.get("SHEETY_TOKEN")}"
        }

    def add_row(self, data: dict):
        config_post = {
            "workout" : {**data},
        }
        response = requests.post(url=self.endpoint, json=config_post, headers=self.headers)
        print(response.text)

import requests

class Agify:
    def __init__(self):
        self.url = "https://api.agify.io"
        self.data_age = None

    def find_age(self, name):
        parameters = {
            "name": name
        }
        response = requests.get(url=self.url, params=parameters)
        response.raise_for_status()
        self.data_age = response.json()["age"]
        return self.data_age

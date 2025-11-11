import requests

class Genderize:
    def __init__(self):
        self.url = "https://api.genderize.io"
        self.data_gender = None

    def find_gender(self, name):
        parameters = {
            "name": name
        }
        response = requests.get(url=self.url, params=parameters)
        response.raise_for_status()
        self.data_gender = response.json()["gender"]
        return self.data_gender

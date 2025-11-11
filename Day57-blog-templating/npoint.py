import requests

class Npoint:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.npoint_get = requests.get(url=self.url)
        self.npoint_get.raise_for_status()
        self.get_info_npoint = self.npoint_get.json()
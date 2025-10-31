import requests
from bs4 import BeautifulSoup

URL_ZILLOW = "https://appbrewery.github.io/Zillow-Clone/"

class SiteSrape:
    def __init__(self):
        self.header = {
        'Accept-Language' : "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        }
        self.response = requests.get(url=URL_ZILLOW, headers=self.header)
        self.web_page = self.response.text
        self.web = BeautifulSoup(self.web_page, "html.parser")
        self.list_prices = []
        self.list_of_address = []
        self.list_of_links = []

    def find_requests(self):
        announcements = self.web.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        for announcement in announcements:
            price = announcement.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").getText().strip().split("+")[0]
            address_of_announcement = announcement.find(name="address").getText().strip()
            link_of_announcement = announcement.find(name="a", attrs="StyledPropertyCardDataArea-anchor")
            self.list_prices.append(price.split("/")[0])
            self.list_of_address.append(address_of_announcement)
            self.list_of_links.append(link_of_announcement.get("href"))



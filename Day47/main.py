import requests
from bs4 import BeautifulSoup
from send_email import EMAILSENDER
PRICE_SMS = 100
EMAIL_TO_SEND = "fulger.sorin@yahoo.com"
sender = EMAILSENDER()
header = {
    'Accept-Language' : "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=url, headers=header)
web_page = response.text

web = BeautifulSoup(web_page, "html.parser")
price_in_web = int(web.find(name="span", class_="a-price-whole").getText().split(".")[0])

if price_in_web < PRICE_SMS:
    sender.send_email(email_to_send=EMAIL_TO_SEND, price=price_in_web, url=url)



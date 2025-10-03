import requests
import os
from twilio.rest import Client

def print_news():
    if procent >= 5:
        if list_close_price[0] > list_close_price[1]:
            for x in range(0, 3):
                message = client.messages.create(
                    body=f"{STOCK} 🔺{round(procent)}% \n\n Headline: {list_articol_title[x]} \n\n Brief: {list_articol_description[x]}",
                    from_="+17753079413",
                    to=os.environ.get("PHONE_NUMBER")
                )
        elif list_close_price[0] < list_close_price[1]:
            for x in range(0, 3):
                message = client.messages.create(
                    body=f"{STOCK} 🔻{round(procent)}% \n\n Headline: {list_articol_title[x]} \n\n Brief: {list_articol_description[x]}",
                    from_="+17753079413",
                    to=os.environ.get("PHONE_NUMBER")
                )

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_ALPHA_VENTAGE = os.environ.get("KEY_ALPHA_VENTAGE")
API_NEWS = os.environ.get("API_NEWS")
ACCOUNT_SID = "ACc3752f7e9b969e1fbf776d7bdfcaa2e4"
AUTH_TOKEN = os.environ.get("TOKEN")
client = Client(ACCOUNT_SID, AUTH_TOKEN)
list_articol_title = []
list_articol_description = []
parameters={
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" : API_KEY_ALPHA_VENTAGE,
    "outputsize" : "compact"
}
request_alpha_ventage=requests.get(url="https://www.alphavantage.co/query", params=parameters)
request_alpha_ventage.raise_for_status()
data_alpha_ventage = request_alpha_ventage.json()
print(data_alpha_ventage)
list_close_price = []
cnt = 0
for data in data_alpha_ventage["Time Series (Daily)"]:
    cnt +=1
    list_close_price.append(data_alpha_ventage["Time Series (Daily)"][data]["4. close"])
    if cnt == 2:
        break

parameters_news={
    "apiKey" : API_NEWS,
    "q" : "tesla",
    "pageSize" : 3
}
request_news = requests.get(url="https://newsapi.org/v2/everything", params= parameters_news)
request_news.raise_for_status()
data_news= request_news.json()


for news in data_news["articles"]:
    list_articol_title.append(news["title"])
    list_articol_description.append(news["description"])


list_close_price = [float(i) for i in list_close_price]
delta = abs(list_close_price[0] - list_close_price[1])
procent = (delta/list_close_price[1])*100
print_news()


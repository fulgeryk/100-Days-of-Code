import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
LAT = 47.158455
LONG = 27.601442
account_sid = "ACc3752f7e9b969e1fbf776d7bdfcaa2e4"
auth_token = os.environ.get("AUTH_TOKEN_TWILIO")

parameters = {
    "lat" : LAT,
    "lon" : LONG,
    "appid" : API_KEY,
    "cnt" : 4
}
request_weather = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
request_weather.raise_for_status()
data_weather = request_weather.json()

will_rain = False
for id_wet in data_weather["list"]:
    weather_id=id_wet["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, take an umbrella ☂️",
        from_="+17753079413",
        to=os.environ.get("PERSONAL_NUMBER"),
    )
    print(message.status)
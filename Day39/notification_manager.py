import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.SID = os.environ.get("TWILIO_SID")
        self.TOKEN = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.SID, self.TOKEN)

    def send_sms(self, price, from_city, to_city, out_date, return_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only ${price} to fly from {from_city} to {to_city}, on {out_date} until {return_date}",
            from_="+17753079413",
            to=os.environ.get("PHONE_NUMBER")
        )
        print(message.status)

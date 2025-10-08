import os
from twilio.rest import Client
import smtplib

class NotificationManager:
    def __init__(self):
        self.SID = os.environ.get("TWILIO_SID")
        self.TOKEN = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.SID, self.TOKEN)
        self.my_email="fulger.sorin@yahoo.com"
        self.password = os.environ.get("FLIGHT_SEARCH")

    def send_sms(self, price, from_city, to_city, out_date, return_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only ${price} to fly from {from_city} to {to_city}, on {out_date} until {return_date}",
            from_="+17753079413",
            to=os.environ.get("PHONE_NUMBER")
        )
        print(message.status)

    def send_mail(self, email_to_send, price, from_city, to_city, stops, out_date, return_date):
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            msg = (f"From: {self.my_email}\nTo: {email_to_send}\nSubject: LOW PRICE ALERT TO {to_city}\n\n "
                   f"LOW PRICE ALERT! Only GBP{price} to fly from {from_city} to {to_city}, "
                   f"with {stops} stop(s) departing on {out_date} and returning on {return_date}")
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=email_to_send,
                msg=msg
            )

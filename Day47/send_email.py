import os
from dotenv import load_dotenv
load_dotenv()
import smtplib

class EMAILSENDER:
    def __init__(self):
        self.my_email = os.environ.get("MY_EMAIL")
        self.my_password = os.environ.get("MY_PASSWORD")

    def send_email(self, email_to_send, price, url):
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            msg = (f"From: {self.my_email}\nTo: {email_to_send}\nSubject: AMAZON PRICE ALERT\n\n "
                   f"LOW PRICE ALERT! Only ${price}, you can order now from {url}")
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=email_to_send,
                msg=msg
            )

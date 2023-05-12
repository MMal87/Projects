import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from twilio.rest import Client



my_number = os.getenv("MY_PHONE_NUMBER")



class TextMessageSender():
    def __init__(self, my_number):
        self.my_number = my_number
        self.twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
    def send_message(self):    
        client = Client(self.twilio_sid, self.twilio_auth)
        message = client.messages.create(
            body="Thank you! Your order was placed and will be delivered before 18:52",
            from_=self.twilio_phone,
            to=my_number)
        self.message_sid = message.sid

        return self.message_sid



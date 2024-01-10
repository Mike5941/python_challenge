from twilio.rest import Client

TWILIO_SID = "ACefd86674a6dfcda85e0080f6576674cb"
TWILIO_AUTH = "40f93e2540f3a090b0554f8bd727697a"
TWILIO_VIRTUAL_NUMBER = "+13609269052"
MY_PHONE_NUMBER = "+821074439500"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=MY_PHONE_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

from twilio.rest import Client
import smtplib

MY_EMAIL = "enjoy5941@gmail.com"
MY_PASSWORD = "mgppaqzvkncibvlj"

TWILIO_SID = "ACefd86674a6dfcda85e0080f6576674cb"
TWILIO_AUTH_TOKEN = "40f93e2540f3a090b0554f8bd727697a"
TWILIO_VIRTUAL_NUMBER = "+13609269052"
TWILIO_VERIFIED_NUMBER = "+821074439500"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, emails, url):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{url}".encode('utf-8')
                )

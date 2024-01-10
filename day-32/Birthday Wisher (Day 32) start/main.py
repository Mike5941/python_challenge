import smtplib
import datetime as dt
from random import choice

def send_email():
    my_email = "enjoy5941@gmail.com"
    password = "sojddwjhdbkpdmwj"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mike9159@naver.com",
                            msg=f"Subject:Today's quotes\n\n{quote}"
                            )


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("quotes.txt", "r") as data_file:
        all_quote = data_file.readlines()
        quote = choice(all_quote)
    send_email()



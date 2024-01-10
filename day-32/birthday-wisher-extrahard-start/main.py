##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "enjoy5941@gmail.com"
MY_PASSWORD = "sojddwjhdbkpdmwj"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
month_day = f"{today.month}-{today.day}"
year_month_day = f"{today.year}-{today.month}-{today.day}"
current_time = today.time()

data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
birthday_person = [data for data in birthday_data if month_day == f"{data['month']}-{data['day']}"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in birthday_person:
    name = person['name']
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", ) as letter_data:
        contents = letter_data.read()
        contents = contents.replace(PLACEHOLDER, name)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="mike9159@naver.com",
                            msg=f"Subject:To {name}\n\n{contents}"
                            )







# 4. Send the letter generated in step 3 to that person's email address.





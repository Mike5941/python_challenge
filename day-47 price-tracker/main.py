import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "enjoy5941@gmail.com"
MY_PASSWORD = "oekrthmqaobxmhon"

response = requests.get("https://search.shopping.naver.com/catalog/32713692618?adId=nad-a001-02-000000190939054&channel=naver.search.pc.npla&query=%EB%A1%9C%EC%A7%80%ED%85%8D%EB%A7%88%EC%9A%B0%EC%8A%A4&NaPm=ct%3Dla1utk0o%7Cci%3D0AC0001dqQfx%2D2cDyvnP%7Ctr%3Dpla%7Chk%3De2c2e9c72e2210dc1d0b871d74a055c6d35045a5&cid=0AC0001dqQfx-2cDyvnP")
product = response.text

soup = BeautifulSoup(product, 'html.parser')

price_data = soup.find("em", class_="lowestPrice_num__A5gM9")
price = price_data.get_text().replace(",", "")

if int(price) < 140809:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="mike9159@naver.com",
            msg=f"{price} gogo sing"
        )


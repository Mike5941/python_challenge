import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
hot_100 = response.text

soup = BeautifulSoup(hot_100, 'html.parser')

print(soup.prettify())

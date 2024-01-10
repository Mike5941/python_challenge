from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

count = 1
for movie in soup.find_all("h3", class_="title"):
    movies = movie.get_text()
    with open("movies.txt", "a") as file:
        if movies == "12: The Godfather Part II":
            file.write(f"{count}){movies.split(':')[1]}\n")
        else:
            file.write(f"{count}){movies.split(')')[1]}\n")











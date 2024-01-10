import requests

from pprint import pprint

API_KEY = "ae4c62af3546ad1a3d578c84e2eea81b"
URL = "https://api.themoviedb.org/3"


def search_movie(title):
    query = {
        "api_key": API_KEY,
        "query": title,
    }
    response = requests.get(
        url=f"{URL}/search/movie", params=query)
    result = response.json()['results']
    return result


def get_details(movie_id):
    query = {
        "api_key": API_KEY,
    }
    response = requests.get(
        url=f"{URL}/movie/{movie_id}", params=query)
    result = response.json()

    return result

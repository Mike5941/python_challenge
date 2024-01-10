import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from math import floor

load_dotenv()

GENDER = "male"
WEIGHT_KG = "60"
HEIGHT_CM = "163"
AGE = "27"

APP_ID = os.environ.get("NT_APP_ID")
API_KEY = os.environ.get("NT_API_KEY")
EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")


exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=parameters)
exercise_data = response.json()["exercises"][0]

exercise_name = exercise_data['name']
exercise_min = round(exercise_data['duration_min'])
exercise_calories = floor(exercise_data['nf_calories'])


if exercise_min >= 60:
    duration_hour = floor(exercise_min / 60)
    duration_minute = exercise_min % 60
    if duration_hour < 10:
        duration_hour = f"0{duration_hour}"
        exercise_min = f"{duration_hour}:{duration_minute}"
else:
    if exercise_min < 10:
        exercise_min = f"00:0{exercise_min}"

#
today = datetime.now()
date = today.strftime('%d/%m/%Y')
time = today.strftime('%X')

SHEET_ENDPOINT=os.environ.get("SHEET_ENDPOINT")

sheet_parameters = {
    "sheet1": {
        "date": f"{date}",
        "time": f"{time}",
        "exercise": f"{exercise_name.title()}",
        "duration": f"{exercise_min}",
        "calories": f"{exercise_calories}"
    }
}

bearer_headers = {
    "Authorization": "Bearer Your_TOKEN"
}

sheet_response = requests.post(
    url=SHEET_ENDPOINT,
    json=sheet_parameters,
    headers=bearer_headers
)

print(sheet_response.json())
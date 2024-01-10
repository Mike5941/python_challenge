import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "ACefd86674a6dfcda85e0080f6576674cb"
auth_token = "40f93e2540f3a090b0554f8bd727697a"

weather_params = {
    "lat": 37.5683,
    "lon": 126.9778,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 890:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_='+13609269052',
        to='+8201074439500'
    )
    print(message.status)


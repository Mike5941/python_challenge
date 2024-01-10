import requests
from datetime import datetime

USERNAME = "wonsoong"
TOKEN = "dfaf2fasd34dsaf"
GRAPH_ID = "graph1"
NAME = "Coding Graph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now().date()

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many time did you study today?"),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

edit_data = {
    "quantity": "1",
}
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.put(url=f"{pixel_creation_endpoint}/20221018", headers=headers, json=edit_data)

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
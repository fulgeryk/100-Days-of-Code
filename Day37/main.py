import requests
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()
USERNAME = "fulger"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params= {
    "token" : os.environ.get("TOKEN_PIXELA"),
    "username" : "fulger",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "commit",
    "type" : "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN" : os.environ.get("TOKEN_PIXELA")
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_post_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How manny commit today ? ")
}

response = requests.post(url=pixel_post_endpoint, json=pixel_post_config, headers=headers)
print(response.text)

pixel_put_and_delete_endpoint = f"{pixel_post_endpoint}/{today.strftime("%Y%m%d")}"

pixel_put_config = {
    "quantity" : "3"
}

response = requests.put(url=pixel_put_and_delete_endpoint, json=pixel_put_config, headers=headers)
print(response.text)

#For delete
response = requests.delete(url=pixel_put_and_delete_endpoint, headers=headers)
print(response.text)
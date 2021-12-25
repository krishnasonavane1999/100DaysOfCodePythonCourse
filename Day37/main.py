import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USER_NAME = #Your custom username
TOKEN = #Your custom key
GRAPH_ID = #unique graph Id

user_params = {
	
	"token": TOKEN,
	"username": USER_NAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"


graph_params = {
	
	"id": GRAPH_ID,
	"name": USER_NAME,
	"unit": "kilometers",
	"type": "int",
	"color": "momiji" # red
}

auth_headers = {

	"X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=auth_headers)

# print(graph_response)

add_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()


pixel_params = {
	"date": today.strftime("%Y%m%d"),
	"quantity": "5"
}

# add_pixel = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=auth_headers)


update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

upate_pixel_params = {
	
	"quantity": "10"
}

update_response = requests.put(url=update_endpoint, json=upate_pixel_params, headers=auth_headers)

print(update_response.text)
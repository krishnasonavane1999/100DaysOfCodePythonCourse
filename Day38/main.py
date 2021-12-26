import requests
import json
import datetime
APP_ID = Your App id
NURI_API_KEY = your APi key
GENDER = your gender
AGE = your age
WEIGHT = your weight
HEIGHT = your height

auth_headers = {
	
	"x-app-id": APP_ID,
	"x-app-key": NURI_API_KEY
}


text_input_from_user = input("Which workout you ant to register?")

parameters = {
	
	"query": text_input_from_user,
	"gender": GENDER,
	"weight_kg": WEIGHT,
	"height_cm": HEIGHT,
	"age": AGE
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_endpoint, json=parameters, headers=auth_headers)

data = json.loads(response.text)
EXERCISE = str(data["exercises"][0]["name"].title())
DURATION = str(data["exercises"][0]["duration_min"])
CALORIES = str(data["exercises"][0]["nf_calories"])


today = datetime.datetime.now()
workout_data = {

	"workout":{
		"date": today.strftime("%d/%m/%Y"),
		"time": today.strftime("%I:%M:%S"),
		"exercise": EXERCISE,
		"duration": DURATION,
		"calories": CALORIES

	}
	
}

sheet_endpoint = Your google sheet endpoint for sheety.com

data_from_sheet = requests.get(sheet_endpoint)

data_from_sheet = json.loads(data_from_sheet.text)

put_data_in_sheet_response = requests.post(url=sheet_endpoint, json=workout_data)

print(put_data_in_sheet_response)
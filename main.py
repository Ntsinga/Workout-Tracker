import requests
from datetime import datetime
import os

NTRX_APP_ID = os.environ['NTRX_APP_ID']
NTRX_API_KEY = os.environ['NTRX_API_KEY']
SHEETY_AUTHORIZATION_TOKEN = os.environ['SHEETY_AUTHORIZATION_TOKEN']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

sheety_header = {
    "Authorization": f"Bearer {SHEETY_AUTHORIZATION_TOKEN}"
}

today = datetime.now()
time = today.time()

nutritionix_headers = {
    "x-app-id": NTRX_APP_ID,
    "x-app-key": NTRX_API_KEY
}

input = {
    "query": input("Tell me which exercise you did:")
}

response = requests.post(nutritionix_endpoint, headers=nutritionix_headers, json=input)
print(response.json())
workouts = response.json()['exercises']
print(workouts)
print(type(today.time()))

for workout in workouts:
    workout_data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": time.strftime("%H:%M:%S"),
            "exercise": workout['name'].title(),
            "duration": workout['duration_min'],
            "calories": workout['nf_calories']
        }
    }

    response2 = requests.post(SHEETY_ENDPOINT, json=workout_data, headers=sheety_header)
    print(response2.status_code)



import os,json
from datetime import datetime
import requests

GENDER = "male"
WEIGHT_KG = 113.39
HEIGHT_CM = 172.72
AGE = 33

DIR = os.path.dirname(os.path.realpath(__file__))

def get_data(file):
    try:
        with open(file,'r',encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def set_data(data,file):
    # self.sort()
    with open(file,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4)

config_file = os.path.join(DIR,'config.json')
print(config_file)
config_data = get_data(config_file)
print(config_data)

APP_ID = config_data['APP_ID']
API_KEY = config_data['API_KEY']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a66265942c4341dc164e0bd22797f82a/workouts/workouts"

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
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {config_data['API_KEY']}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)

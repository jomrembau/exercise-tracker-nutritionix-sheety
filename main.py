import requests
import datetime as dt

# ------------------ CONFIG ------------------
APP_ID = "YOUR_NUTRITIONIX_APP_ID"
API_KEY = "YOUR_NUTRITIONIX_API_KEY"

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 171
AGE = 41
SHEETY_URL = "YOUR_SHEETY_ENDPOINT_URL"
SHEETY_TOKEN = "YOUR_SHEETY_BEARER_TOKEN"
# --------------------------------------------

# Get current date and time
today = dt.datetime.now()
date = str(today.date())
time = today.strftime("%H:%M:%S")

# Nutritionix API endpoint
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

# User input
query = input("Which exercises have you completed? ")

params = {
    "query": query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Send request to Nutritionix
response = requests.post(url=URL, json=params, headers=headers)
data = response.json()

# Parse response safely
if data.get("exercises"):
    exercise_data = data["exercises"][0]
    exercise = exercise_data.get("user_input", "Unknown").title()
    duration = exercise_data.get("duration_min", 0)
    calories = exercise_data.get("nf_calories", 0)
else:
    print("No exercise data found.")
    exit()

# Prepare data for Sheety
workout = {
    "date": date,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
}

data_to_send = {"workout": workout}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# Send data to Sheety
sheety_response = requests.post(url=SHEETY_URL, json=data_to_send, headers=sheety_headers)

print(sheety_response.text)

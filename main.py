import requests
import datetime as dt

# --- USER INPUT REQUIRED ---
APP_ID = "YOUR_NUTRITIONIX_APP_ID"
API_KEY = "YOUR_NUTRITIONIX_API_KEY"
SHEETY_URL = "YOUR_SHEETY_PROJECT_URL"

GENDER = "male"       # Change if needed
WEIGHT_KG = 70        # Enter your weight in kg
HEIGHT_CM = 170       # Enter your height in cm
AGE = 30              # Enter your age

# Get current date and time
today = dt.datetime.now()
date = str(today.date())
time = today.strftime("%H:%M:%S")

# Nutritionix API URL
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Ask user which exercises they completed
query = input("Which exercises have you completed? ")

params = {
    "query": query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Get exercise data from Nutritionix
response = requests.post(url=URL, json=params, headers=header)
data = response.json()

exercise = data["exercises"][0]["user_input"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

# Prepare workout data for Sheety
workout = {
    "date": date,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
}

data_to_send = {
    "workout": workout
}

# Send data to Sheety
sheety_response = requests.post(url=SHEETY_URL, json=data_to_send)

print(sheety_response.text)

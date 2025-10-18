Exercise Tracker – Nutritionix & Sheety
Description

* This Python script allows you to track your workouts easily. You input the exercises you’ve completed, and the script retrieves details like duration and calories burned from the Nutritionix API. It then logs the data into a Google Sheet via Sheety, automatically recording the date and time.

Features

* Tracks exercise name, duration, and calories.

* Automatically records date and time.

* Logs data into Google Sheets for easy tracking.

* Uses Nutritionix API for accurate exercise info.

* Simple, interactive console input.

Requirements

* Python 3.x

* requests library

* Nutritionix account (APP_ID & API_KEY)

* Sheety account connected to a Google Sheet

Setup

* Clone this repository.

* Install required Python libraries:

* pip install requests


Set up a Google Sheet and connect it to Sheety.

* Update the APP_ID, API_KEY, and SHEETY_URL in the script.

Run the script:

* python exercise_tracker.py

Usage

* Run the script in a terminal or IDE.

* Enter the exercises you completed when prompted, e.g., I ran for 20 minutes.

* The script will fetch exercise data and log it to your Google Sheet.

* Check your Google Sheet to see the new entry.

License

This project is open-source and free to use.

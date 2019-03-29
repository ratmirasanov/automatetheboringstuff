#! python3
# quick_цeather.py -- Prints the weather for a location from the command line.

import json
import sys
import requests


# Compute location from command line arguments.
if len(sys.argv) < 2:

    print("Usage: quick_weather.py location")
    sys.exit()

LOCATION = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
URL = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3" % LOCATION
RESPONSE = requests.get(URL)
RESPONSE.raise_for_status()

# Load JSON data into a Python variable.
WEATHER_DATA = json.loads(RESPONSE.text)
# Print weather descriptions.
W = WEATHER_DATA["list"]
print("Current weather in %s:" % LOCATION)
print(W[0]["weather"][0]["main"], "-", W[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(W[1]["weather"][0]["main"], "-", W[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(W[2]["weather"][0]["main"], "-", W[2]["weather"][0]["description"])

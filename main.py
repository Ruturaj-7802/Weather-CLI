import argparse # to write user-friendly CLI (Command Line Interfaces)
import pyfiglet # ASCII R text to normal text
from simple_chalk import chalk
import requests

# API key for openweathermap
API_KEY = "d9378740f38293f0daaab4374cd45bb5"

# Base URL for openweather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Map the weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}
# construct API URL with query parameters
parser = argparse.ArgumentParser(description="Check the weather for a certain city/country")
parser.add_argument("Country", help="The country/city to check the weather for")
args = parser.parse_args()

url =f"{BASE_URL}?q={args.Country}&appid={API_KEY}&units=metric"

# Make API request and parse response using requests module
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error : Unabel to retrieve weather information"))
    exit()

# parsing the json response from API and extract the weather information
data = response.json()

# get information from response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# construct the output wiht weather icon
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon}   {description}\n"
output += f"Temperature : {temperature}°C\n"
output += f"Feels like : {feels_like}°C\n"

# print the output
print(chalk.green(output))





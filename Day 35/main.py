import requests

API_KEY = "e2b5f5c48ac8cf5cacb4db9925b42256"
URL = "https://api.openweathermap.org/data/3.0/onecall"

# Just getting the hourly forecast
parameters = {
    "lat": 27.496031,
    "lon": -109.932838,
    "appid": API_KEY,
    "exclud": "current,minutley,daily"
}

response = requests.get(url=URL, params=parameters)
weather_data = response.json()
hourly_data = weather_data["hourly"]
# # Getting the first hour weather id
# print(hourly_data[0]["weather"][0]["id"])

# The next 12 hours of weather data
weather_slice = hourly_data[:12]

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
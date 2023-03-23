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
print(weather_data)
import requests

API_KEY = "e2b5f5c48ac8cf5cacb4db9925b42256"
URL = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": 27.496031,
    "lon": -109.932838,
    "appid": API_KEY
}

response = requests.get(url=URL, params=parameters)
weather_data = response.json()
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    raise Exception("Bad response from ISS API")

response.raise_for_status()
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
import requests
import random
from datetime import datetime
# URL endpoint
URL = "https://api.sunrise-sunset.org/json"

lat = random.randint(-10000000, 10000000) / 100000
lng = random.randint(-10000000, 10000000) / 100000

# date = datetime.now()
# day = date.weekday() 

# My solution
response = requests.get(url=URL+f"?lat={lat}&lng={lng}")
data = response.json()['results']
#print(data)

# Angela solution
parameters = {
    "lat" : random.randint(-10000000, 10000000) / 100000,
    "lng" : random.randint(-10000000, 10000000) / 100000,
    "formatted" : 0
}

response = requests.get(url=URL, params=parameters)
data = response.json()['results']
sunrise = data['sunrise'].split("T")[1].split(":")[0]
sunset = data['sunset'].split("T")[1].split(":")[0]
# print just the hour
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)
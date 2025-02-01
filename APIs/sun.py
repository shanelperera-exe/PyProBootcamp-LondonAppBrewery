import requests
from datetime import datetime

MY_LAT = 7.082892
MY_LNG = 79.868396

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise}")
print(f"Sunrise: {sunset}")

time_now = datetime.now().hour
print(f"Current time: {time_now}")
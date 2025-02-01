import requests

API_KEY = "7632d04c00729cd14bc518918391f9db"

MY_LAT = 7.082863
MY_LONG = 79.868407

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
print(data)
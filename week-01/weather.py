import requests as requests
import json

city_id = '3054643'
api_key = '03621b4c221f18cdd23317b7aa5152e8'
parameters = {"id": city_id, "appid": api_key, "units": "metric"}
url = 'https://api.openweathermap.org/data/2.5/weather'

response = requests.get(url, params = parameters)
print(response.status_code)
print(response.headers["content-type"])
weather_info = response.json()
print(weather_info)
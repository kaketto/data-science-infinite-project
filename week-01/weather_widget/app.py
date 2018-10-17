import pandas as pd
import numpy as np
import requests as requests
import json
from flask import Flask, render_template
app = Flask(__name__)

# city_list_json = './city.list.json'
# df = pd.read_json(city_list_json)

city_id = '3054643'
api_key = '03621b4c221f18cdd23317b7aa5152e8'
parameters = {"id": city_id, "appid": api_key, "units": "metric"}
url = 'https://api.openweathermap.org/data/2.5/weather'
icon_url = 'http://openweathermap.org/img/w/'

@app.route("/", methods= ['GET'])
def weather_app():
    response = requests.get(url, params = parameters)
    # print(response.status_code)
    # print(response.headers["content-type"])
    weather_info = response.json()
    # print(weather_info)
    icon_url_with_iconcode = icon_url + weather_info['weather'][0]['icon'] + '.png'
    print(icon_url)
    return render_template('weather.html', city=weather_info['name'], description=weather_info['weather'][0]['description'], icon_src=icon_url_with_iconcode,
    temperature=weather_info['main']['temp'], wind=weather_info['wind']['speed'], humidity=weather_info['main']['humidity'], pressure=weather_info['main']['pressure'])

if __name__ == '__main__':
    app.run(debug=True)
import pandas as pd
import numpy as np
import requests as requests
import json
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

city_list_json = './city.list.json'
df = pd.read_json(city_list_json)

api_key = '03621b4c221f18cdd23317b7aa5152e8'
url = 'https://api.openweathermap.org/data/2.5/weather'
icon_url = 'http://openweathermap.org/img/w/'

@app.route("/", methods= ['GET'])
@app.route("/city", methods= ['POST'])
def weather_app():
    if request.method == 'POST':
        selected_city = request.form['city']
        city_id = df[df['name'] == selected_city]['id'].values[0]
    else:
        city_id = '3054643'
    parameters = {"id": city_id, "appid": api_key, "units": "metric"}
    response = requests.get(url, params = parameters)
    weather_info = response.json()
    icon_url_with_iconcode = icon_url + weather_info['weather'][0]['icon'] + '.png'
    return render_template('weather.html', city=weather_info['name'], description=weather_info['weather'][0]['description'], icon_src=icon_url_with_iconcode,
        temperature=weather_info['main']['temp'], wind=weather_info['wind']['speed'], humidity=weather_info['main']['humidity'], pressure=weather_info['main']['pressure'])

if __name__ == '__main__':
    app.run(debug=True)

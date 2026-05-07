# This is a Python CLI program that will provide weather data for a user-input city

import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, redirect


load_dotenv()
# import API key from .env (.env part of gitignore for API key security)
WEATHER_KEY = os.getenv('WEATHER_API_KEY')
app = Flask(__name__)

def get_weather(city):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&limit=1&appid={WEATHER_KEY}"
    geo_data = requests.get(geo_url).json()
    # print(geo_data)

    #safety check
    if not geo_data:
        return None
    
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # weather url
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={WEATHER_KEY}"

    #get API data
    weather_data = requests.get(weather_url).json()

    return {
        "city": city.title(),
        "temperature": weather_data['main']['temp'],
        "feels_like": weather_data['main']['feels_like'],
        "conditions": weather_data['weather'][0]['main']
    }

@app.route('/')
def redirect_to_weather():
    return redirect('/weather')

@app.route('/weather')
def weather():
    city = request.args.get('city', 'New York')
    if not city:
        return jsonify({"error": "Please provide a city parameter"}), 400
    
    result = get_weather(city)
    if not result:
        return jsonify({"error": f"City '{city}' not found"}), 404
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

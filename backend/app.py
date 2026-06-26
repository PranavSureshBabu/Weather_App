from flask import Flask, jsonify, send_from_directory
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import os

from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__,
            static_folder="../frontend/dist",
            static_url_path="")
CORS(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.route("/api")
def home():
    return jsonify({
        "message": "Weather API Running"
    })


@app.route("/api/weather/<city>")
def get_weather(city):

    try:

        geolocator = Nominatim(
            user_agent="weather_app"
        )

        location = geolocator.geocode(city)

        if location is None:
            return jsonify({
                "error": "Invalid City Please Try again"
            }), 404

        obj = TimezoneFinder()

        timezone = obj.timezone_at(
            lng=location.longitude,
            lat=location.latitude
        )

        home_timezone = pytz.timezone(timezone)

        local_time = datetime.now(
            home_timezone
        ).strftime("%I:%M %p")

        api_url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={API_KEY}"
        )

        response = requests.get(api_url)

        json_data = response.json()

        if json_data.get("cod") != 200:
            return jsonify({
                "error": json_data.get("error","Invalid City. Please Try again."
                )
            }), 400

        weather_data = {
            "city": city.title(),

            "country": json_data["sys"]["country"],

            "time": local_time,

            "temperature": int(json_data["main"]["temp"] - 273.15),

            "feels_like": int(json_data["main"]["feels_like"] - 273.15),

            "condition": json_data["weather"][0]["main"],

            "description": json_data["weather"][0]["description"].title(),

            "humidity": json_data["main"]["humidity"],

            "pressure": json_data["main"]["pressure"],

            "wind": json_data["wind"]["speed"],

            "visibility": int(json_data["visibility"] / 1000)
            }

        return jsonify(weather_data)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/")
def serve_vue():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)

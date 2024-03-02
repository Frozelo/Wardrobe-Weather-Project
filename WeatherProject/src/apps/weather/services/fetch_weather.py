import datetime
import os

import requests
from dotenv import load_dotenv
from src.apps.client.services.fetch_client import fetch_client_info

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')


def get_current_season():
    now = datetime.datetime.now()
    month = now.month
    seasons = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter"
    }
    return seasons.get(month, "Unknown")


def fetch_weather_by_client(client, region, city):

    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric')
    weather_data = response.json()
    return weather_data, response

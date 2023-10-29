import os

import requests
from django.shortcuts import render
from dotenv import load_dotenv
from src.client.models import Client
from src.wardrobe.models import Clothes

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')


# TODO Start developing a prototype of my algorithm. Pay attention to optimization!
def fetch_weather_logic(request, user):
    client = Client.objects.get(user=user)
    city = client.city
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric')
    weather_data = response.json()
    return city, response, weather_data



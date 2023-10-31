import os

import requests
from django.shortcuts import render
from dotenv import load_dotenv
from src.client.models import Client
from src.wardrobe.models import Clothes

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')


def get_client(user):
    return Client.objects.only('region', 'city').get(user=user)


# TODO Start developing a prototype of my algorithm. Pay attention to optimization!

def fetch_weather_and_client_info_logic(user):
    client = get_client(user)
    region = client.region
    city = client.city
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric')
    weather_data = response.json()
    return client, region, city, weather_data, response

import requests
from django.shortcuts import render

from src.client.models import Client
from src.wardrobe.models import Clothes
from src.weather.api_keys import weather_api_key


# TODO Start developing a prototype of my algorithm. Pay attention to optimization!
def fetch_weather_logic(request, user):
    client = Client.objects.get(user=user)
    city = client.city

    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric')
    weather_data = response.json()
    return city, response, weather_data


def get_city_for_client(request):
    city = request.POST.get('city')
    user_instance = request.user

    try:
        client = Client.objects.get(user=user_instance)
        client.city = city
        client.save()

    except:
        client = Client(user=user_instance, city=city)
        client.save()

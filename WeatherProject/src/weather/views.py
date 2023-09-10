import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from src.client.models import Client
from src.wardrobe.logiv import outfit_logic
from src.weather.api_keys import weather_api_key
from src.weather.logic import get_city_for_client, fetch_weather_logic


# Create your views here.


def get_city_for_client_view(request):
    if request.method == 'POST':
        get_city_for_client(request)
    return render(request, 'weather/city.html')


# @login_required
def fetch_weather(request):
    if request.method == 'POST':
        user, city, response, weather_data = fetch_weather_logic(request)
        print(response.status_code)
        if response.status_code == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            outfit_logic(user, temperature, style='sport')
            return render(request, 'weather/weather.html', {
                'city': city,
                'temperature': temperature,
                'humidity': humidity
            })
    return render(request, 'weather/weather.html')

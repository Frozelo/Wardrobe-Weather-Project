import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from src.client.models import Client
from src.weather.api_keys import weather_api_key
from src.weather.logic import get_city_for_client


# Create your views here.


def get_city_for_client_view(request):
    if request.method == 'POST':
        get_city_for_client(request)
    return render(request, 'weather/city.html')


@login_required
def fetch_weather(request):
    if request.method == 'POST':
        user = request.user
        client = Client.objects.get(user=user)
        city = client.city

        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric')

        if response.status_code == 200:
            weather_data = response.json()

            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            return render(request, 'weather/weather.html', {
                'city': city,
                'temperature': temperature,
                'humidity': humidity
            })

    return render(request, 'weather/weather.html')

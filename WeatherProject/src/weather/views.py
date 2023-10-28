import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from src.client.models import Client
from src.wardrobe.logiv import outfit_logic
from src.weather.api_keys import weather_api_key
from src.weather.logic import fetch_weather_logic
from src.weather.models import Season
from src.weather.middlewares.extract_user_middleware import ExtractUserMiddleware



# @login_required
# TODO Where is no logic!!!!
def fetch_weather(request):
    # Получаем пользователя из middleware
    user = request.custom_user
    city, response, weather_data = fetch_weather_logic(request, user)

    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        season_id = request.POST.get('season')
        style_id = request.POST.get('style')
        request.session['season'] = season_id
        request.session['style'] = style_id
        request.session['temperature'] = temperature
        humidity = weather_data['main']['humidity']
        clothes_list_2 = outfit_logic(user, temperature, season_id, style_id)
        print(clothes_list_2)
        return render(request, 'weather/weather.html', {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'user': user,
            'clothes_list_2': clothes_list_2,
        })

    return render(request, 'weather/weather.html', {'user': user})


def get_clothes_set_view(request):
    user = request.custom_user
    season = request.session.get('season')
    style = request.session.get('style')
    temperature = request.session.get('temperature')
    print(user)
    print(temperature)
    print(f'{season} - {style}')
    return render(request, 'weather/outfit_set.html')

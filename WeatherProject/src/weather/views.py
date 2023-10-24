import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from src.client.models import Client
from src.wardrobe.logiv import outfit_logic
from src.weather.api_keys import weather_api_key
from src.weather.logic import get_city_for_client, fetch_weather_logic
from src.weather.models import Season
from src.weather.middlewares.extract_user_middleware import ExtractUserMiddleware
# Create your views here.


def get_city_for_client_view(request):
    if request.method == 'POST':
        get_city_for_client(request)
    return render(request, 'weather/city.html')


# @login_required
def fetch_weather(request):
    # Получаем пользователя из middleware
    user = request.custom_user
    city, response, weather_data = fetch_weather_logic(request, user)

    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        request.session['temperature'] = temperature
        humidity = weather_data['main']['humidity']
        season_id = request.POST.get('season')
        style_id = request.POST.get('style')
        clothes_list_2 = outfit_logic(user, temperature, season_id, style_id)
        print(clothes_list_2)
        return render(request, 'weather/weather.html', {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'user': user,
            'clothes_list_2': clothes_list_2,  # Добавьте эту переменную в контекст
        })

    return render(request, 'weather/weather.html', {'user': user})



# def get_clothes_set_view(request, season_id, style_id):
#     user = request.custom_user
#     temperature = request.session.get('temperature')
#     print(season_id)
#     print(style_id)
#     clothes_list = outfit_logic(user, temperature, season_id, style_id)
#
#     return render(request, 'weather/outfit_set.html', {'clothes_list': clothes_list})

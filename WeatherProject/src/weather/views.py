from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from src.wardrobe.services.outfit_generation_logic import outfit_logic
from src.weather.services.fetch_weather_logic import fetch_weather_and_client_info_logic


# @login_required
# TODO Where is no logic!!!!
def fetch_weather(request):
    # Получаем пользователя из middleware
    user = request.custom_user
    _, _, city, weather_data, response = fetch_weather_and_client_info_logic(user)

    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        style_id = request.POST.get('style')
        request.session['style'] = style_id
        request.session['temperature'] = temperature
        humidity = weather_data['main']['humidity']
        clothes_list_2 = outfit_logic(user, temperature, style_id)
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

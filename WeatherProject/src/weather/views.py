from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from src.wardrobe.services.outfit_generation_logic import outfit_logic
from src.wardrobe.services.test_file import OutfitLogic
from src.weather.services.fetch_weather import fetch_weather_and_client_info_logic


@login_required
# TODO Where is no logic!!!!
def fetch_weather(request):
    if request.method == 'POST':
        user = request.custom_user
        _, _, city, weather_data, response = fetch_weather_and_client_info_logic(user)

        if response.status_code == 200 and 'main' in weather_data:
            temperature = weather_data['main'].get('temp')
            humidity = weather_data['main'].get('humidity')

            if temperature is not None and humidity is not None:
                style_id = request.POST.get('style')
                request.session['style'] = style_id
                request.session['temperature'] = temperature

                body_part_list = {
                    'head': request.POST.get('head'),
                    'upper_body': request.POST.get('upper_body'),
                    'upper_body_secondary': request.POST.get('upper_body_secondary'),
                    'bottom_body': request.POST.get('bottom_body'),
                    'bottom_body_secondary': request.POST.get('bottom_body_secondary'),
                    'feet': request.POST.get('feet')
                }

                outfit_logic_instance = OutfitLogic(user, temperature, style_id, body_part_list)
                clothes_list = outfit_logic_instance.outfit_logic()
                print(clothes_list)
                return render(request, 'weather/weather.html', {
                    'city': city,
                    'temperature': temperature,
                    'humidity': humidity,
                    'user': user,
                    'clothes_list_2': clothes_list,
                })

    return render(request, 'weather/weather.html', {'user': request.custom_user})




def get_clothes_set_view(request):
    user = request.custom_user
    season = request.session.get('season')
    style = request.session.get('style')
    temperature = request.session.get('temperature')
    print(user)
    print(temperature)
    print(f'{season} - {style}')
    return render(request, 'weather/outfit_set.html')

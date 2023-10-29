from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from src.client.forms import AvatarUploadForm
from src.client.services.client_city_save import get_city_for_client
from src.wardrobe.models import group_clothes_by_type
from src.weather.services.fetch_weather_logic import fetch_weather_logic


@login_required
def profile(request):
    user = request.user
    _, _, weather_data = fetch_weather_logic(request, user)
    clothes_by_type = group_clothes_by_type(user)
    first_name = user.first_name
    last_name = user.last_name
    client = user.client
    region = client.region
    city = client.city
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.client)
        if form.is_valid():
            form.save()
    else:
        form = AvatarUploadForm(instance=client)
    context = {'user': user,
               'name': first_name,
               'last_name': last_name,
               'region': region,
               'city': city,
               'clothes_by_type': clothes_by_type,
               'weather_data': weather_data,
               'form': form
               }
    return render(request, 'user/profile.html', context)


def settings_view(request):
    return render(request, 'user/settings.html')


def get_city_for_client_view(request):
    if request.method == 'POST':
        get_city_for_client(request)
    return render(request, 'weather/city.html')

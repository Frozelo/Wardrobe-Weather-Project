from django.contrib.auth import logout
from django.db.models import Sum
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from src.apps.client.services.client_city_save import get_city_for_client
from .models import Client
from .services.fetch_client import fetch_client_info
from src.apps.wardrobe.models import group_clothes_by_type, Preset
from src.apps.weather.services.fetch_weather import fetch_weather_by_client
from .services.user_auth import user_auth_logic
from django.shortcuts import render, redirect, get_object_or_404
from .services.fetch_client import get_client
from src.apps.wardrobe.services.preset_logic import likes_logic, delete_preset_logic
from .services.avatar_upload import avatar_upload_form_logic
from ...core.services import get_objects, filter_objects


def user_auth_view(request):
    if request.method == 'POST':
        return user_auth_logic(request)
    else:
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return render(request, 'user/auth.html')


def user_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_auth')


@login_required
def profile(request):
    user = request.user
    client = get_object_or_404(Client, user=user)
    region, city = fetch_client_info(client)
    weather_data, _ = fetch_weather_by_client(client, region, city)
    clothes_by_type = group_clothes_by_type(user)
    first_name = user.first_name
    last_name = user.last_name
    form = avatar_upload_form_logic(request, client)
    context = {'client': client,
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


# TODO Database logic in view - make core service
def saved_presets_view(request):
    user = request.user
    presets = filter_objects(obj=Preset.objects,
                             owner=user,
                             select_related=(),
                             ).annotate(total_likes=Sum('likes'))

    context = {
        "presets": presets
    }
    return render(request, 'user/saved_presets.html', context=context)

def delete_preset_view(request):
    delete_preset_logic(request)
    return redirect('/profile/saved-presets')


def like_preset_view(request):
    if request.method == "POST":
        likes_logic(preset_id=request.POST.get("preset_id"))
    return HttpResponse(content={"message": "good"})


def get_city_for_client_view(request):
    if request.method == 'POST':
        get_city_for_client(request)
    return render(request, 'user/settings.html')

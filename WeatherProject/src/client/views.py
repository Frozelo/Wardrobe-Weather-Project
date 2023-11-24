from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from src.client.forms import AvatarUploadForm
from src.client.models import Client
from src.client.services.client_city_save import get_city_for_client
from src.client.services.user_auth import user_auth_logic
from src.wardrobe.models import group_clothes_by_type
from src.weather.services.fetch_weather_logic import fetch_weather_and_client_info_logic

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Client


# TODO - The client model problem.
#  I need to decide what to do with the client model (I want to merge fields with the user model)
def user_auth_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if Client.objects.filter(user=user).exists():
                    return redirect('profile')
                else:
                    return redirect('settings')
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except KeyError as e:
            return JsonResponse({'error': e, 'message': 'Missing credentials'}, status=400)
        except Exception as e:
            return JsonResponse({'error': e, 'message': 'An error occurred'}, status=500)

    return render(request, 'user/auth.html')


def user_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_auth')


@login_required
def profile(request):
    user = request.user
    client, region, city, weather_data, _ = fetch_weather_and_client_info_logic(user)
    clothes_by_type = group_clothes_by_type(user)
    first_name = user.first_name
    last_name = user.last_name
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.client)
        if form.is_valid():
            form.save()
    else:
        form = AvatarUploadForm(instance=client)
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


def get_city_for_client_view(request):
    if request.method == 'POST':
        get_city_for_client(request)
    return render(request, 'user/settings.html')

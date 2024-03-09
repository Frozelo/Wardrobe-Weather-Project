from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Case, When
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from src.apps.wardrobe.services.clothes_crud import delete_clothes_logic, save_clothes_logic, update_clothes_logic
from src.apps.wardrobe.serializers import ClothesSerializer, UserSerializer
from src.apps.wardrobe.services.preset_logic import save_preset
from src.apps.weather.models import Season
from src.apps.weather.permissions import IsAuthenticatedOrReadOnly
from src.apps.weather.services.fetch_sesason import get_all_seasons
from src.core.services import all_objects


def auth_view(request):
    return render(request, 'oauth.html')


@login_required
def save_clothes_view(request):
    seasons_list = get_all_seasons()
    print(seasons_list)
    if request.method == 'POST':
        save_clothes_logic(request)
    return render(request, 'wardrobe/wardrobe.html', {'all_seasons': seasons_list})


def delete_clothes_view(request):
    if request.method == 'POST':
        delete_clothes_logic(request)
    return redirect('/profile/')


def update_clothes_view(request):
    if request.method == 'POST':
        update_clothes_logic(request)
    return redirect('/profile/')


def save_clothes_preset(request):
    if request.method == 'POST':
        save_preset(request)
    return redirect('/profile/')

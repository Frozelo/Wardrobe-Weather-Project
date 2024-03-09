from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from src.apps.wardrobe.services.wardrobe_weather_processor import WeatherWardrobeRequestProcessor


@login_required
def wardrobe_weather_view(request):
    wardrobe_weather_fetcher = WeatherWardrobeRequestProcessor(request)
    weather_data_context = wardrobe_weather_fetcher.fetch_weather_data()

    return render(request, 'weather/weather.html', weather_data_context)

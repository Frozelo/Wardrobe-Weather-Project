from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from src.wardrobe.services.wardrobe_weather_processor import WeatherRequestProcessor


@login_required
def wardrobe_weather_view(request):
    wardrobe_weather_fetcher = WeatherRequestProcessor(request)
    context = wardrobe_weather_fetcher.fetch_weather_data()

    return render(request, 'weather/weather.html', context)

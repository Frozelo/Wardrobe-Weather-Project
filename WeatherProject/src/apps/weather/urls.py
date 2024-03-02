from django.urls import path
from . import views

urlpatterns = [
    path('', views.wardrobe_weather_view, name='fetch_weather'),

]
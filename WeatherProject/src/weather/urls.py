from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_weather, name='fetch_weather'),
]
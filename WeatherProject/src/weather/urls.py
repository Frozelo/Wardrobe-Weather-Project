from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_weather, name='fetch_weather'),
    path('get_clothes_set/', views.get_clothes_set_view, name='get_clothes_set_view'),
]
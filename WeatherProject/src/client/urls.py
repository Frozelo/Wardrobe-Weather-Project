from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    path('city/save', views.get_city_for_client_view, name = 'get_city_for_client_view'),
    path('logout', LogoutView.as_view(), name='logout'),
]
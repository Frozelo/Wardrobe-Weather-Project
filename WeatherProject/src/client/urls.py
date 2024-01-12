from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.user_auth_view, name='user_auth'),
    path('logout/', views.user_logout_view, name='logout'),
    path('settings/', views.settings_view, name='settings_list'),
    path('saved-presets', views.saved_presets_view),
    path('city/save', views.get_city_for_client_view, name='get_city_for_client_view'),
    path('like_preset/', views.like_preset_view, name='like_preset'),
]

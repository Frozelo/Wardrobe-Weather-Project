from django.urls import path
from . import views

urlpatterns = [
    path('save', views.save_clothes_view, name='save_clothes_view'),
]
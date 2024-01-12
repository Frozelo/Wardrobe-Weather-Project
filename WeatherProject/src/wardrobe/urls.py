from django.urls import path
from . import views

urlpatterns = [
    path('save', views.save_clothes_view, name='save_clothes_view'),
    path('update', views.update_clothes_view, name='update_clothes_view'),
    path('delete', views.delete_clothes_view, name='delete_clothes_view'),
    path('preset/save', views.save_preset, name = 'save_preset'),
]
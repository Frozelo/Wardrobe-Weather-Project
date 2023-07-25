"""WeatherProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from src.wardrobe.views import ClothesViewSet, UserViewSet, save_clothes_view, \
    auth_view
from src.weather.views import get_city_for_client_view

router_cloths = SimpleRouter()
router_users = SimpleRouter()
router_cloths.register(r'wardrobe', ClothesViewSet, basename='wardrobe')
router_users.register(r'users', UserViewSet)
# router_cloths.register('', ClothesJSONViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth_view),
    path('weather/', include('src.weather.urls')),
    path('api/', include(router_cloths.urls)),
    path('api/', include(router_users.urls)),
    path('wardrobe/save/', save_clothes_view, name='save_clothes_view'),
    path('city/save/', get_city_for_client_view, name='get_city_for_client_view')
]




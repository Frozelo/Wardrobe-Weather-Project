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
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from src.apps.wardrobe.views import UserViewSet, auth_view


router_users = SimpleRouter()
router_users.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth_view),
    path('weather/', include('src.apps.weather.urls')),
    path('wardrobe/', include('src.apps.wardrobe.urls')),
    path('profile/', include('src.apps.client.urls')),
    path('api/v1/', include('src.api.urls')),
    path("__debug__/", include("debug_toolbar.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

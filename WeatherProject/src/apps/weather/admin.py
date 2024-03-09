from django.contrib import admin

# Register your models here.
from src.apps.weather.models import Season

admin.site.register(Season)
from django.contrib import admin

# Register your models here.
from src.apps.client.models import Client

admin.site.register(Client)
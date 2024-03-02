from django.contrib import admin

# Register your models here.
from src.apps.wardrobe.models import Clothes, TypeOfClothes, Style, Preset

admin.site.register(Clothes)
admin.site.register(TypeOfClothes)
admin.site.register(Style)
admin.site.register(Preset)
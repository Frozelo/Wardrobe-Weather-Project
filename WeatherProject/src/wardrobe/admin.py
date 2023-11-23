from django.contrib import admin

# Register your models here.
from src.wardrobe.models import Clothes, TypeOfClothes, Style, Preset

admin.site.register(Clothes)
admin.site.register(TypeOfClothes)
admin.site.register(Style)
admin.site.register(Preset)
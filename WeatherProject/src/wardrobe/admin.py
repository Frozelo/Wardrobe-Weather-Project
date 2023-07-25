from django.contrib import admin

# Register your models here.
from src.wardrobe.models import Clothes, TypeOfClothes, Clothes_JSON

admin.site.register(Clothes)
admin.site.register(TypeOfClothes)
admin.site.register(Clothes_JSON)
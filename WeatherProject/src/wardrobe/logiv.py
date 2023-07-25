import json

from django.contrib.auth.decorators import login_required

from src.wardrobe.models import Clothes, Clothes_JSON




@login_required
def save_clothes_logic(request):
    description = request.POST.get('description')
    brand = request.POST.get('brand')
    owner_id = request.user.id
    clothes = Clothes(description_of_clothes=description, brand=brand, owner_id=owner_id)
    clothes.save()

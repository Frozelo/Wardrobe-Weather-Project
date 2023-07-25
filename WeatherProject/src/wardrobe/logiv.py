import json

from django.contrib.auth.decorators import login_required

from src.wardrobe.models import Clothes, Clothes_JSON


# @Incomplete: My json with clothes is updates if only  redirect to wardrobe/dict/check (this address
# calls the function for checking and saving). So I need to create a new trigger which will check the dictionary
# originality and if it necessary, save a new dict.
# Also, json saving works incorrect: If I have an original json that doesn't match a
# previous entry, it is created anew, which is not correct It has to be overwritten"


def personal_wardrobe_dict():
    clothes = Clothes.objects.all()
    wardrobe_dict = {}

    for cloth in clothes:
        owner_id = cloth.owner_id
        description = cloth.description_of_clothes
        type_of_clothes = [type_cloth.type for type_cloth in cloth.type_of_clothes.all()]
        if owner_id not in wardrobe_dict:
            wardrobe_dict[owner_id] = []

        wardrobe_dict[owner_id].append({
            'description': description,
            'type_of_clothes': type_of_clothes
        })

    json_data = json.dumps(wardrobe_dict)
    clothes_json, created = Clothes_JSON.objects.get_or_create(pk=14)
    clothes_json.json_dict = json_data
    clothes_json.save()

    return wardrobe_dict


@login_required
def save_clothes_logic(request):
    description = request.POST.get('description')
    brand = request.POST.get('brand')
    owner_id = request.user.id
    clothes = Clothes(description_of_clothes=description, brand=brand, owner_id=owner_id)
    clothes.save()

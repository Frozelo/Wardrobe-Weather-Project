import json

from django.contrib.auth.decorators import login_required

from src.wardrobe.models import Clothes, Clothes_JSON

# Add all fields to be saved in database. Make query optimization
# COMPLETE. _____________
# TODO Decide what type of clothing information retention is best.
# IN PROGRESS. I think we should start by comparing the temperature and the current state of the season.
# If all requirements are met, then display the usable items.
from src.weather.logic import fetch_weather_logic


@login_required
def save_clothes_logic(request):
    description = request.POST.get('description')
    brand = request.POST.get('brand')
    owner_id = request.user.id
    season_ids = request.POST.getlist('season')
    temperature_range = request.POST.get('optimal_temp_range')
    min_temp, max_temp = map(float, temperature_range.split(':'))
    dict_to_save = {
        'min_temp': min_temp,
        'max_temp': max_temp
    }
    clothes = Clothes.objects.create(description_of_clothes=description, brand=brand, owner_id=owner_id,
                                     optimal_temperature=dict_to_save)
    clothes.season.set(season_ids)
    # clothes = Clothes(description_of_clothes=description, brand=brand, owner_id=owner_id,
    #                   optimal_temperature=dict_to_save)
    # clothes.save()
    # print(temperature_range)


def outfit_logic(request, temperature):
    clothes = Clothes.objects.filter(owner=request.user.id).select_related('owner')

    for item in clothes:
        optimal_temperature = item.optimal_temperature
        min_temp = float(optimal_temperature.get("min_temp"))
        max_temp = float(optimal_temperature.get("max_temp"))

        if min_temp <= temperature <= max_temp:
            print(
                f"{item.description_of_clothes} - Success. "
                f"Minimal temperature:{min_temp}; Maximum temperature:{max_temp}"
            )
        else:
            print(
                f"{item.description_of_clothes} - Unsuccessful. "
                f"Minimal temperature:{min_temp}; Maximum temperature:{max_temp}")

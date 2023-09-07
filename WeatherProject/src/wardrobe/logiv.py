import itertools

from django.contrib.auth.decorators import login_required

from src.wardrobe.models import Clothes, Clothes_JSON

# Add all fields to be saved in database. Make query optimization
# COMPLETE. _____________
# TODO Decide what type of clothing information retention is best.
# IN PROGRESS. I think we should start by comparing the temperature and the current state of the season.
# If all requirements are met, then display the usable items.
from src.weather.logic import fetch_weather_logic


def outfit_logic(user, temperature):
    """Version 1 - My logic"""
    clothes = Clothes.objects.filter(owner=user.id).select_related('owner').select_related('type_of_clothes')

    clothes_list_2 = {
        'Head': {
            'req': False,
            'status': False,
            'item': None

        },
        'Jacket': {
            'req': True,
            'status': False,
            'item': None

        },
        'T-shirt': {
            'req': True,
            'status': False,
            'item': None

        },
        'Pants': {
            'req': True,
            'status': False,
            'item': None

        },
        'Socks': {
            'req': True,
            'status': False,
            'item': None
        },

        'Sneakers': {
            'req': True,
            'status': False,
            'item': None
        }
    }

    for item in clothes:
        optimal_temperature = item.optimal_temperature
        if is_suitable_temperature(item, temperature):
            if not clothes_list_2[item.type_of_clothes.type]['status']:
                clothes_list_2[item.type_of_clothes.type]['status'] = True
                clothes_list_2[item.type_of_clothes.type]['item'] = item.description_of_clothes

    not_found_types = {k for k, v in clothes_list_2.items() if v['req'] and not v['status']}

    if not_found_types:
        return False

    # print(clothes_list_2)
    print(clothes_list_2)
# def outfit_logic_2(user, temperature):
#     """Version 2 - need to figure out"""
#     clothes = Clothes.objects.filter(owner=user.id).select_related('owner')
#
#     # Фильтруем подходящие вещи в соответствии с температурой
#     suitable_clothes = [item for item in clothes if is_suitable_temperature(item, temperature)]
#
#     # Разделяем вещи по категориям
#     categories = {
#         'Jacket': [],
#         'T-shirt': [],
#         'Pants': [],
#         'Socks': [],
#         'Sneakers': []
#     }
#
#     for item in suitable_clothes:
#         category = item.type_of_clothes.type
#         categories[category].append(item)
#
#     # Генерируем возможные комбинации для каждой категории
#     outfit_combinations = list(
#         itertools.product(categories['Jacket'], categories['T-shirt'], categories['Pants'], categories['Socks'],
#                           categories['Sneakers']))
#
#     # Получаем первые 5 аутфитов из списка комбинаций
#     outfits = outfit_combinations[:5]
#
#     for i, outfit in enumerate(outfits):
#         print(f'Outfit {i + 1}:')
#         for item in outfit:
#             print(f'- {item.description_of_clothes}')


def is_suitable_temperature(item, temperature):
    optimal_temperature = item.optimal_temperature
    return optimal_temperature and float(optimal_temperature.get("min_temp", 0)) <= temperature <= float(
        optimal_temperature.get("max_temp", 0))

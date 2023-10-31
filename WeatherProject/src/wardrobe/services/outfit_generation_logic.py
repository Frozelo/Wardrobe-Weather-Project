import datetime
import logging
from typing import Union, Dict, Optional

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from src.wardrobe.models import Clothes

current_season = None

logging.basicConfig(filename='weather.log', level=logging.DEBUG)


def get_season():
    now = datetime.datetime.now()
    month = now.month
    seasons = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter"
    }
    return seasons.get(month, "Unknown")


# TODO I don't think a global variable is a good decision in this logic
def get_current_season():
    global current_season
    if current_season is None:
        current_season = get_season()
    return current_season


def get_suitable_clothes(user, style):
    try:
        return Clothes.objects.defer('brand', 'photo_of_clothes', 'favorites').filter(owner=user).select_related(
            'owner').select_related(
            'type_of_clothes').filter(style__name=style)
    except ObjectDoesNotExist:
        return None
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


def is_suitable_temperature(item, temperature: float) -> bool:
    optimal_temperature = item.optimal_temperature
    return optimal_temperature and float(optimal_temperature.get("min_temp", 0)) <= temperature <= float(
        optimal_temperature.get("max_temp", 0))


def is_suitable_season(item):
    today_season = get_current_season()
    return item.season.filter(season_name=today_season).exists()


def sort_clothes_by_style(clothes, style: str):
    """Returns clothes filtered by the necessary style"""
    return clothes.filter(style__name=style)


# TODO Pay attention to this function because it needs to good queries optimization
# DONE Added a status check of clothes status in dict. If it's true we don't need to call is_suitable function
def fill_clothes_list(clothes, temperature: float, clothes_list: dict):
    """Fills the dictionary with clothing by season temperature and season"""
    for item in clothes:
        if not clothes_list[item.type_of_clothes.type]['status']:
            if is_suitable_temperature(item, temperature) and is_suitable_season(item):
                clothes_list[item.type_of_clothes.type]['status'] = True
                clothes_list[item.type_of_clothes.type]['item'] = item.description_of_clothes


def outfit_logic(user, temperature: float, style: str) -> Union[bool, Dict[str, Union[
    Dict[str, Optional[bool]], Dict[str, Optional[bool]], Dict[str, Optional[bool]], Dict[str, Optional[bool]], Dict[
        str, Optional[bool]], Dict[str, Optional[bool]]]]]:
    """Version 1 - My logic"""
    clothes = get_suitable_clothes(user, style)
    clothes_list = {
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
        },
    }
    filtered_clothes_by_style = sort_clothes_by_style(clothes, style)
    fill_clothes_list(filtered_clothes_by_style, temperature, clothes_list)
    not_found_types = {k for k, v in clothes_list.items() if v['req'] and not v['status']}
    if not_found_types:
        return False
    return clothes_list

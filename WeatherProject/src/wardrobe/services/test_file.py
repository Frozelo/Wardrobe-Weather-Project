import logging
from typing import Union, Dict, Optional
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from src.wardrobe.models import Clothes
from src.weather.services.fetch_weather import get_current_season


class ClothesManager:
    @staticmethod
    def get_clothes_and_filter_by_style(user, style, favorites):
        try:
            queryset = Clothes.objects.filter(
                owner=user,
                style__name=style
            ).select_related('owner', 'type_of_clothes')

            if favorites:
                queryset = queryset.filter(favorites=favorites)

            return queryset.defer('brand', 'photo_of_clothes')
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def is_suitable_temperature(item, temperature: float) -> bool:
        optimal_temperature = item.optimal_temperature
        return optimal_temperature and float(optimal_temperature.get("min_temp", 0)) <= temperature <= float(
            optimal_temperature.get("max_temp", 0))

    @staticmethod
    def is_suitable_season(item, today_season) -> bool:
        return item.season.filter(season_name=today_season).exists()


class OutfitLogic:
    def __init__(self, user, temperature: float, style: str, favorites: bool, body_part_list: dict):
        self.user = user
        self.temperature = temperature
        self.style = style
        self.favorites = favorites
        self.body_part_list = body_part_list
        self.clothes_list = self.initialize_clothes_list()

    def outfit_logic(self):
        filtered_clothes_by_style = ClothesManager.get_clothes_and_filter_by_style(self.user, self.style,
                                                                                   self.favorites)
        today_season = get_current_season()
        self.fill_clothes_list(filtered_clothes_by_style, self.clothes_list, today_season)
        if not self.is_outfit_complete(self.clothes_list):
            return False
        return self.clothes_list

    def initialize_clothes_list(self):
        clothes_list = {}
        for value in self.body_part_list.values():
            clothes_list[value] = {
                'req': False,
                'status': False,
                'item': None
            }
        return clothes_list

    def fill_clothes_list(self, clothes, clothes_list, today_season):
        for item in clothes:
            if clothes_list.get(item.type_of_clothes.type) is not None \
                    and not clothes_list[item.type_of_clothes.type]['status']:
                if ClothesManager.is_suitable_temperature(item, self.temperature) and ClothesManager.is_suitable_season(
                        item, today_season):
                    clothes_list[item.type_of_clothes.type]['status'] = True
                    clothes_list[item.type_of_clothes.type]['item'] = item.description_of_clothes

    @staticmethod
    def is_outfit_complete(clothes_list):
        for key, value in clothes_list.items():
            if value['req'] and not value['status']:
                return False
        return True

from django.core.exceptions import ObjectDoesNotExist
from src.wardrobe.models import Clothes
from src.weather.services.fetch_weather import get_current_season
import logging


class ClothesManager:
    @staticmethod
    def get_clothes_and_filter_by_style(user, style, today_season, favorites):
        try:
            queryset = Clothes.objects.filter(
                owner=user,
                style__name=style,
                season__season_name=today_season,
            ).order_by('rate').select_related('owner', 'type_of_clothes')

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


class OutfitLogic:
    def __init__(self, user, temperature: float, style: str, favorites: bool, body_part_list: dict):
        self.user = user
        self.temperature = temperature
        self.style = style
        self.favorites = favorites
        self.body_part_list = body_part_list
        self.clothes_list = self.initialize_clothes_list()

    def outfit_logic(self):
        today_season = get_current_season()
        filtered_clothes_by_style = ClothesManager.get_clothes_and_filter_by_style(self.user, self.style, today_season,
                                                                                   self.favorites)

        logging.debug(filtered_clothes_by_style)
        self.fill_clothes_list(filtered_clothes_by_style, self.clothes_list)
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

    def fill_clothes_list(self, clothes, clothes_list):
        for item in clothes:
            if clothes_list.get(item.type_of_clothes.type) is not None \
                    and not clothes_list[item.type_of_clothes.type]['status']:
                if ClothesManager.is_suitable_temperature(item, self.temperature):
                    clothes_list[item.type_of_clothes.type]['status'] = True
                    clothes_list[item.type_of_clothes.type]['item'] = item.description_of_clothes

    @staticmethod
    def is_outfit_complete(clothes_list):
        for key, value in clothes_list.items():
            if value['req'] and not value['status']:
                return False
        return True

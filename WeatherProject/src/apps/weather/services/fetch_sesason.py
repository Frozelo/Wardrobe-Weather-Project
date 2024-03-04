from src.apps.weather.models import Season
from src.core.services import all_objects


def get_all_seasons():
    return all_objects(obj=Season.objects,)

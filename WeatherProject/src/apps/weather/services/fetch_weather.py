import datetime
import requests
from src.core.open_weather_api_service import get_weather_api_key_from_dotenv


def get_current_month():
    now = datetime.datetime.now()
    month = now.month
    return month


def get_current_season():
    month = get_current_month()
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


def fetch_weather_by_client(city):
    open_weather_api_key = get_weather_api_key_from_dotenv()
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_api_key}&units=metric')
    weather_data = response.json()
    return weather_data, response

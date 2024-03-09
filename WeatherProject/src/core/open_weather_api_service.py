from dotenv import load_dotenv
import os


def get_weather_api_key_from_dotenv() -> str:
    load_dotenv()
    open_weather_api_key = os.getenv('OPEN_WEATHER_API_KEY')
    return open_weather_api_key

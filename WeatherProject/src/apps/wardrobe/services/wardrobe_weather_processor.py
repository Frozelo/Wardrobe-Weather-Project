from src.apps.client.services.fetch_client import get_client, fetch_client_info
from src.apps.wardrobe.services.test_file import OutfitGenerator
from src.apps.weather.services.fetch_weather import fetch_weather_by_client


class UserClientManager:
    def __init__(self, request):
        self.request = request

    def get_user(self):
        return self.request.custom_user

    def get_client(self, user):
        return get_client(user)

    def fetch_client_location(self, client):
        return fetch_client_info(client)

    def fetch_weather_by_client(self, city):
        return fetch_weather_by_client(city)


class BodyPartListGenerator:
    def get_body_part_list(self, request):
        body_parts = ['head', 'upper_body', 'upper_body_secondary', 'bottom_body', 'bottom_body_secondary', 'feet']
        return {part: request.POST.get(part) for part in body_parts}


class ThirdPartyOptions:
    def get_third_parties_options(self, request):
        favourites_str = request.POST.get('favorites', 'false')
        favourites = favourites_str.lower() == "true"
        return favourites


class WeatherWardrobeRequestProcessor:
    def __init__(self, request):
        self.request = request
        self.user_client_manager = UserClientManager(request)
        self.body_part_list_generator = BodyPartListGenerator()
        self.third_party_options = ThirdPartyOptions()

    def fetch_weather_data(self):
        user = self.user_client_manager.get_user()
        client = self.user_client_manager.get_client(user)
        region, city = self.user_client_manager.fetch_client_location(client)
        weather_data, response = self.user_client_manager.fetch_weather_by_client(city)
        if self.is_weather_data_valid(response, weather_data):
            temperature, humidity = self.extract_temperature_and_humidity(weather_data)
            style_id = self.request.POST.get('style')
            self.update_session_data(temperature, style_id)

            body_part_list = self.generate_body_part_list()
            favorites = self.get_third_party_options()

            clothes_list = self.generate_outfit(user, temperature, style_id, favorites, body_part_list)

            context = self.create_context(city, temperature, humidity, user, clothes_list)
            return context

    def is_weather_data_valid(self, response, weather_data):
        return response.status_code == 200 and 'main' in weather_data

    def extract_temperature_and_humidity(self, weather_data):
        temperature = weather_data['main'].get('temp')
        humidity = weather_data['main'].get('humidity')
        return temperature, humidity

    def update_session_data(self, temperature, style_id):
        self.request.session['style'] = style_id
        self.request.session['temperature'] = temperature

    def generate_body_part_list(self):
        return self.body_part_list_generator.get_body_part_list(self.request)

    def get_third_party_options(self):
        return self.third_party_options.get_third_parties_options(self.request)

    def generate_outfit(self, user, temperature, style_id, favorites, body_part_list):
        outfit_logic_instance = OutfitGenerator(user, temperature, style_id, favorites, body_part_list)
        return outfit_logic_instance.generate_outfit()

    def create_context(self, city, temperature, humidity, user, clothes_list):
        return {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'user': user,
            'clothes_list_2': clothes_list,
        }

from src.wardrobe.services.test_file import OutfitGenerator
from src.weather.services.fetch_weather import fetch_weather_by_client


class WeatherRequestProcessor:
    def __init__(self, request):
        self.request = request

    def fetch_weather_data(self):
        user = self.request.custom_user
        _, city, weather_data, response = fetch_weather_by_client(user)

        if response.status_code == 200 and 'main' in weather_data:
            temperature = weather_data['main'].get('temp')
            humidity = weather_data['main'].get('humidity')

            if temperature is not None and humidity is not None:
                style_id = self.request.POST.get('style')
                self.request.session['style'] = style_id
                self.request.session['temperature'] = temperature

                body_part_list = self.get_body_part_list()

                favorites = self.get_third_parties_options()

                outfit_logic_instance = OutfitGenerator(user, temperature, style_id, favorites, body_part_list)
                clothes_list = outfit_logic_instance.generate_outfit()

                context = {
                    'city': city,
                    'temperature': temperature,
                    'humidity': humidity,
                    'user': user,
                    'clothes_list_2': clothes_list,
                }
                return context

    def get_body_part_list(self):
        body_parts = ['head', 'upper_body', 'upper_body_secondary', 'bottom_body', 'bottom_body_secondary', 'feet']
        return {part: self.request.POST.get(part) for part in body_parts}

    def get_third_parties_options(self):
        favorites = bool(self.request.POST.get('favorites'))
        return favorites

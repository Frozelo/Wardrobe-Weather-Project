from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from src.wardrobe.services.wardrobe_weather_processor import outfit_logic
from src.wardrobe.models import Clothes, TypeOfClothes


class OutfitLogicTestCaseV1(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')

        # Создаем типы одежды для тестирования
        self.jacket_type = TypeOfClothes.objects.create(type='Jacket')
        self.tshirt_type = TypeOfClothes.objects.create(type='T-shirt')
        self.head_type = TypeOfClothes.objects.create(type='Head')
        self.socks_type = TypeOfClothes.objects.create(type='Socks')
        self.sneakers_type = TypeOfClothes.objects.create(type='Sneakers')
        self.pants_type = TypeOfClothes.objects.create(type='Pants')

        # Создаем одежду для тестирования
        self.jacket_clothes = Clothes.objects.create(
            description_of_clothes='Test Jacket',
            type_of_clothes=self.jacket_type,
            owner=self.user,
            optimal_temperature=({"min_temp": 0, "max_temp": 28})
        )
        self.tshirt_clothes = Clothes.objects.create(
            description_of_clothes='Test T-shirt',
            type_of_clothes=self.tshirt_type,
            owner=self.user,
            optimal_temperature=({"min_temp": 15, "max_temp": 30})
        )
        self.head_clothes = Clothes.objects.create(
            description_of_clothes='Test Head',
            type_of_clothes=self.head_type,
            owner=self.user,
            optimal_temperature=({"min_temp": 15, "max_temp": 30})
        )
        self_pants_clothes = Clothes.objects.create(
            description_of_clothes='Test Socks',
            type_of_clothes=self.socks_type,
            owner=self.user,
            optimal_temperature=({"min_temp": 15, "max_temp": 30})
        )
        self.tshirt_clothes = Clothes.objects.create(
            description_of_clothes='Test Sneakers',
            type_of_clothes=self.sneakers_type,
            owner=self.user,
            optimal_temperature=({"min_temp": 15, "max_temp": 30})
        )
        self.tshirt_clothes = Clothes.objects.create(
            description_of_clothes='Test Pants',
            type_of_clothes=self.pants_type,
            owner=self.user,
            optimal_temperature=({"min_temp": 15, "max_temp": 30})
        )

    def test_temperature_ok(self):
        # Проверяем логику для температуры 25 (попадает в условия)
        temperature = 25
        result = outfit_logic(self.user, temperature)
        expected_result = {
            'Head': {
                'req': False,
                'status': True,
                'item': "Test Head"

            },
            'Jacket': {
                'req': True,
                'status': True,
                'item': "Test Jacket"

            },
            'T-shirt': {
                'req': True,
                'status': True,
                'item': "Test T-shirt"

            },
            'Pants': {
                'req': True,
                'status': True,
                'item': "Test Pants"

            },
            'Socks': {
                'req': True,
                'status': True,
                'item': "Test Socks"
            },

            'Sneakers': {
                'req': True,
                'status': True,
                'item': "Test Sneakers"
            }
        }
        self.assertEqual(result, expected_result)
        # Проверяем логику для температуры -10 (не попадает в условия)
        temperature = -10
        result = outfit_logic(self.user, temperature)
        self.assertFalse(result)

    def test_temperature_fail(self):
        pass

    def test_without_req(self):
        pass



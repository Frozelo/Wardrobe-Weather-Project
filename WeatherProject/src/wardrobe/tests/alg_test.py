import json

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from src.wardrobe.logiv import outfit_logic
from src.wardrobe.models import Clothes


class OutfitLogicTestCaseV1(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.staff = User.objects.create(username='test_staff', is_staff=True)
        self.jacket_clothes = Clothes.objects.create(description_of_clothes='New clothes 2', type_of_clothes='Jacket',
                                                     owner=self.user,
                                                     optimal_temperature={"min_temp": -5, "max_temp": 20})
        self.tee_clothes = Clothes.objects.create(description_of_clothes='Handmade T-shirt cool',
                                                  type_of_clothes='T-shirt',
                                                  owner=self.user,
                                                  optimal_temperature={"min_temp": -5, "max_temp": 20})
        self.pants_clothes = Clothes.objects.create(description_of_clothes='New Clothes', type_of_clothes='Pants',
                                                    owner=self.user,
                                                    optimal_temperature={"min_temp": -5, "max_temp": 20})
        self.socks_clothes = Clothes.objects.create(description_of_clothes='White Socks Adidas',
                                                    type_of_clothes='Socks',
                                                    owner=self.user,
                                                    optimal_temperature={"min_temp": -5, "max_temp": 20})
        self.sneakers_clothes = Clothes.objects.create(description_of_clothes='555', type_of_clothes='Sneakers',
                                                       owner=self.user,
                                                       optimal_temperature={"min_temp": -5, "max_temp": 20})
        self.temperature = 50

    def test_get(self):
        clothes_list_2 = {
            'Head': {
                'req': False,
                'status': False,
                'item': None

            },
            'Jacket': {
                'req': True,
                'status': True,
                'item': "New clothes 2"

            },
            'T-shirt': {
                'req': True,
                'status': True,
                'item': "Handmade T-shirt cool"

            },
            'Pants': {
                'req': True,
                'status': True,
                'item': "New Clothes"

            },
            'Socks': {
                'req': True,
                'status': True,
                'item': "White Socks Adidas"
            },

            'Sneakers': {
                'req': True,
                'status': True,
                'item': "555"
            }
        }
        result = outfit_logic(self.temperature)

        # Сравниваем полученный результат с ожидаемым
        self.assertDictEqual(result, clothes_list_2)

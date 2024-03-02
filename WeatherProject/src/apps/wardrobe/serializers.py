from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from src.apps.wardrobe.models import Clothes


class UserSerializer(ModelSerializer):
    clothes_favorites_count = serializers.IntegerField(read_only=True)
    clothes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'clothes_favorites_count', 'clothes_count']


class ClothesSerializer(ModelSerializer):
    type_of_clothes = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()

    class Meta:
        model = Clothes
        fields = ('id', 'brand', 'owner', 'type_of_clothes', 'optimal_temperature')






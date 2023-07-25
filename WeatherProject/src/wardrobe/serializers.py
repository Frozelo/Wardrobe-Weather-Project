from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from src.wardrobe.models import Clothes, TypeOfClothes, Clothes_JSON


class UserSerializer(ModelSerializer):
    clothes_favorites_count = serializers.IntegerField(read_only=True)
    clothes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'clothes_favorites_count', 'clothes_count']


class TypeOfClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfClothes
        fields = ('type',)


class ClothesSerializer(ModelSerializer):
    type_of_clothes = TypeOfClothesSerializer(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Clothes
        fields = ('id', 'brand', 'owner', 'type_of_clothes')



class ClothesJSONSerializer(ModelSerializer):
    class Meta:
        model = Clothes_JSON
        fields = ['json_dict']

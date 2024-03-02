from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from src.apps.wardrobe.models import Clothes


class WardrobeClothesSerializer(ModelSerializer):
    type_of_clothes = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()

    class Meta:
        model = Clothes
        fields = ('id', 'brand', 'owner', 'type_of_clothes')

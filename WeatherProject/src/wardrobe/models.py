from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from src.weather.models import Season


class TypeOfClothes(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.type}'


class Style(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    type_of_clothes = models.ForeignKey(TypeOfClothes, on_delete=models.SET_NULL, related_name='type_of_clothes',
                                        null=True, blank=True)
    description_of_clothes = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    season = models.ManyToManyField(Season, blank=True)
    style = models.ManyToManyField(Style, blank=True)
    optimal_temperature = models.JSONField()
    photo_of_clothes = models.ImageField(upload_to='media/wardrobe', null=True, blank=True)
    favorites = models.BooleanField(default=False)

    def clean(self):
        super(Clothes, self).clean()
        if not isinstance(self.optimal_temperature.get("min_temp"), (int, float)):
            raise ValidationError("Минимальное значение оптимальной температуры должно быть числом")
        if not isinstance(self.optimal_temperature.get("max_temp"), (int, float)):
            raise ValidationError("Максимальное значение оптимальной температуры должно быть числом")
        elif self.optimal_temperature.get('min_temp') > self.optimal_temperature.get('max_temp'):
            raise ValueError('Минимальная температура не может быть выше максимальной')

    def __str__(self):
        return f'{self.description_of_clothes} - {self.type_of_clothes} {self.owner}'


class Clothes_JSON(models.Model):
    json_dict = models.JSONField()

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


def group_clothes_by_type(user):
    clothes = Clothes.objects.filter(owner=user.id).select_related('owner').prefetch_related(
        'type_of_clothes')
    clothes_by_type = {}
    for item in clothes:
        type_name = item.type_of_clothes.type
        if type_name in clothes_by_type:
            clothes_by_type[type_name].append(item)
        else:
            clothes_by_type[type_name] = [item]

    return clothes_by_type


class Clothes(models.Model):
    type_of_clothes = models.ForeignKey(TypeOfClothes, on_delete=models.SET_NULL, related_name='type_of_clothes',
                                        null=True, blank=True)
    description_of_clothes = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    season = models.ManyToManyField(Season, blank=True)
    style = models.ManyToManyField(Style, blank=True)
    optimal_temperature = models.JSONField(blank=True)
    photo_of_clothes = models.ImageField(upload_to='wardrobe/clothes', null=True, blank=True)
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


class Preset(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True)
    clothes_dict = models.JSONField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.owner} - {self.name}"

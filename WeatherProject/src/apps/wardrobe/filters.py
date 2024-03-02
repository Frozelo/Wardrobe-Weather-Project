import django_filters
from django_filters import FilterSet, CharFilter
from .models import Clothes


class ClothesFilter(django_filters.FilterSet):
    type_of_clothes = django_filters.CharFilter(field_name='type_of_clothes__type', lookup_expr='icontains')
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='icontains')
    favorites = django_filters.BooleanFilter(field_name='favorites')

    class Meta:
        model = Clothes
        fields = ['type_of_clothes', 'brand', 'favorites']

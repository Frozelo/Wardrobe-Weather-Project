from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Case, When
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from src.wardrobe.services.clothes_CRUD_operations import delete_clothes_logic, save_clothes_logic
from src.wardrobe.models import Clothes
from src.wardrobe.serializers import ClothesSerializer, UserSerializer
from src.weather.models import Season
from src.weather.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().annotate(clothes_favorites_count=Count(Case(When(clothes__favorites=True, then=1))),
                                           clothes_count=Count('clothes'))
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Finish the queries' optimization. It adds 2 more queries in case when we perform user filter.
# COMPLETE? Strange thing..... need to write about it accurately.
class ClothesViewSet(ModelViewSet):
    queryset = Clothes.objects.all().select_related('owner').select_related('type_of_clothes')
    serializer_class = ClothesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'brand']
    search_fields = ['brand', 'type_of_clothes__type', 'favorites', 'description_of_clothes']
    filterset_fields = ['id', 'owner', 'brand', 'type_of_clothes__type', 'favorites']



def auth_view(request):
    return render(request, 'oauth.html')


@login_required
def save_clothes_view(request):
    all_seasons = Season.objects.all()
    if request.method == 'POST':
        save_clothes_logic(request)
    return render(request, 'wardrobe/wardrobe.html', {'all_seasons': all_seasons})


def delete_clothes_view(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        print(item_id)
        delete_clothes_logic(request)
    return redirect('/profile/')



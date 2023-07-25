from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Case, When
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from src.wardrobe.logiv import personal_wardrobe_dict, save_clothes_logic
from src.wardrobe.models import Clothes, Clothes_JSON
from src.wardrobe.serializers import ClothesSerializer, UserSerializer, ClothesJSONSerializer
from src.weather.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().annotate(clothes_favorites_count=Count(Case(When(clothes__favorites=True, then=1))),
                                           clothes_count=Count('clothes'))
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClothesViewSet(ModelViewSet):
    queryset = Clothes.objects.all().prefetch_related('owner').prefetch_related('type_of_clothes')
    serializer_class = ClothesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'brand']
    search_fields = ['brand', 'type_of_clothes__type', 'favorites', 'description_of_clothes']
    filterset_fields = ['id', 'owner', 'brand', 'type_of_clothes__type', 'favorites']


class ClothesJSONViewSet(ModelViewSet):
    queryset = Clothes_JSON.objects.all()
    serializer_class = ClothesJSONSerializer


def auth_view(request):
    return render(request, 'oauth.html')


def wardrobe_dict_view(request):
    wardrobe_dict = personal_wardrobe_dict()
    return JsonResponse(wardrobe_dict, safe=False)


@login_required
def save_clothes_view(request):
    if request.method == 'POST':
        save_clothes_logic(request)
    return render(request, 'wardrobe/wardrobe.html')

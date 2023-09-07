from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Case, When
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from src.wardrobe.logiv import save_clothes_logic
from src.wardrobe.models import Clothes, Clothes_JSON
from src.wardrobe.serializers import ClothesSerializer, UserSerializer
from src.weather.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().annotate(clothes_favorites_count=Count(Case(When(clothes__favorites=True, then=1))),
                                           clothes_count=Count('clothes'))
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# TODO Finish the queries optimization. It adds 2 more queries in case when we perform user filter.
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
    if request.method == 'POST':
        save_clothes_logic(request)
    return render(request, 'wardrobe/wardrobe.html')

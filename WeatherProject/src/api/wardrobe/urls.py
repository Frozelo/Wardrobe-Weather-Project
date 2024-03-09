from django.urls import path, re_path
from src.api.wardrobe.views import ClothesListView, ClothesDetailView

urlpatterns = [
    path('clothes/', ClothesListView.as_view(), name='clothes-list'),
    path('clothes/<int:item_id>/', ClothesDetailView.as_view(), name='clothes-detail'),
]
from django.urls import path, include

urlpatterns = [
    path('wardrobe/', include('src.api.wardrobe.urls'))
]
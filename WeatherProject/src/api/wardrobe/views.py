from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from src.apps.wardrobe.models import Clothes
from src.apps.wardrobe.serializers import ClothesSerializer

# TODO Database logic in view, make core view
from src.core.services import filter_objects


class ClothesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        clothes = filter_objects(Clothes.objects, owner=request.user)
        serializer = ClothesSerializer(clothes, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# TODO Make permission "IsAdminOrOwner" for put method
class ClothesDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, item_id):
        return get_object_or_404(Clothes, id=item_id, owner=self.request.user)

    def get(self, request, item_id):
        clothes = self.get_object(item_id)
        serializer = ClothesSerializer(clothes)
        return JsonResponse(serializer.data)

    def put(self, request, item_id):
        clothes = self.get_object(item_id)
        serializer = ClothesSerializer(clothes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, item_id):
        clothes = self.get_object(item_id)
        clothes.delete()
        return JsonResponse({'message': 'Предмет успешно удален'})

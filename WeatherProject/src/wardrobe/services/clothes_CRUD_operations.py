from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

from src.lib.permissions import IsAdminOrOwner
from src.wardrobe.models import Clothes


@login_required
def save_clothes_logic(request):
    description = request.POST.get('description')
    brand = request.POST.get('brand')
    owner_id = request.user.id
    season_ids = request.POST.getlist('season')
    style_ids = request.POST.getlist('style')
    temperature_range = request.POST.get('optimal_temp_range')
    min_temp, max_temp = map(float, temperature_range.split(':'))
    dict_to_save = {
        'min_temp': min_temp,
        'max_temp': max_temp
    }
    clothes = Clothes.objects.create(description_of_clothes=description, brand=brand, owner_id=owner_id,
                                     optimal_temperature=dict_to_save)
    clothes.season.set(season_ids)
    clothes.style.set(style_ids)


@permission_classes([IsAdminOrOwner])
def delete_clothes_logic(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        print(item_id)
        try:
            item = Clothes.objects.get(pk=item_id)
            item.delete()
            response_data = {'message': 'Предмет успешно удален'}
            print('Предмет успешно удален')
        except Clothes.DoesNotExist:
            response_data = {'message': 'Предмет не найден'}
        return JsonResponse(response_data)
    else:
        response_data = {'message': 'Недопустимый запрос'}
        return JsonResponse(response_data, status=400)


# TODO Optimization and season, style update
@permission_classes([IsAdminOrOwner])
def update_clothes_logic(request):
    response_data = {'message': 'Ошибка при обновлении предмета'}
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        print(item_id)
        try:
            clothes = get_object_or_404(Clothes, id=item_id, owner=request.user)
            description = request.POST.get('description', clothes.description_of_clothes)
            brand = request.POST.get('brand', clothes.brand)
            season_ids = request.POST.getlist('season')
            style_ids = request.POST.getlist('style')
            temperature_range = request.POST.get('optimal_temp_range')
            min_temp, max_temp = map(float, temperature_range.split(':'))
            clothes.description_of_clothes = description
            clothes.brand = brand
            clothes.optimal_temperature = {'min_temp': min_temp, 'max_temp': max_temp}
            clothes.season.set(season_ids)
            clothes.style.set(style_ids)
            clothes.save()
            response_data = {'message': 'Предмет успешно обновлен'}
        except ValueError:
            response_data = {'message': 'Ошибка при обработке температурного диапазона'}
    else:
        response_data = {'message': 'Метод запроса не поддерживается'}

    return JsonResponse(response_data)

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from src.core.services import get_objects, create_objects
from src.lib.permissions import IsAdminOrOwner
from src.apps.wardrobe.models import Clothes
from src.core.services import set_related_objects, update_objects
from src.core.request_service import get_request_params


@login_required
def save_clothes_logic(request):
    owner_id = request.user.id
    params = get_request_params(request,
                                params=('description_of_clothes',
                                        'brand',
                                        'optimal_temperature'
                                        ))
    season_ids = request.POST.getlist('season')
    style_ids = request.POST.getlist('style')
    clothes = create_objects(obj=Clothes.objects,
                             owner_id=owner_id,
                             **params,
                             )
    set_related_objects(obj=clothes,
                        season=season_ids,
                        style=style_ids
                        )


@permission_classes([IsAdminOrOwner])
def delete_clothes_logic(request):
    params = get_request_params(request,
                                params=('id',
                                ))
    try:
        item = get_objects(obj=Clothes.objects,
                           **params)
        item.delete()
        response_data = {'message': 'Предмет успешно удален'}
        print('Предмет успешно удален')
    except Clothes.DoesNotExist:
        response_data = {'message': 'Предмет не найден'}
    return JsonResponse(response_data)


# TODO Optimization and season, style update
@permission_classes([IsAdminOrOwner])
def update_clothes_logic(request):
    item_id = request.POST.get('id')
    try:
        clothes = get_object_or_404(Clothes, id=item_id, owner=request.user)
        params = get_request_params(request,
                                    params=('description_of_clothes',
                                            'brand',
                                            'optimal_temperature'
                                            ))
        season_ids = request.POST.getlist('season')
        style_ids = request.POST.getlist('style')
        update_objects(obj=clothes,
                       **params,
                       )
        set_related_objects(obj=clothes,
                            season=season_ids,
                            style=style_ids
                            )

        clothes.save()
        response_data = {'message': 'Предмет успешно обновлен'}
    except ValueError:
        response_data = {'message': 'Ошибка при обработке температурного диапазона'}

    return JsonResponse(response_data)

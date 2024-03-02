from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from src.apps.wardrobe.models import Preset
from src.core.services import create_objects, get_objects


def save_preset(request):
    if request.method == 'POST':
        owner = request.user
        clothes_dict = request.POST.get('clothes_list')
        preset_name = request.POST.get('preset_name')

        if clothes_dict and preset_name:
            create_objects(obj=Preset.objects,
                           owner=owner,
                           clothes_dict=clothes_dict,
                           name=preset_name, )

            return JsonResponse({'status_code': 200, 'message': 'Success'})
        else:
            return JsonResponse({'status_code': 400, 'message': 'Invalid data received'})
    else:
        return JsonResponse({'status_code': 405, 'message': 'Method Not Allowed'})


def delete_preset_logic(request):
    preset_id = request.POST.get('preset_id')
    try:
        presete = get_objects(obj=Preset.objects,
                              pk=preset_id, )
        presete.delete()
        response_data = {'message': 'Предмет успешно удален'}
        print('Предмет успешно удален')
    except Preset.DoesNotExist:
        response_data = {'message': 'Предмет не найден'}
    return JsonResponse(response_data)


def likes_logic(preset_id):
    try:
        preset = get_object_or_404(Preset, id=preset_id)
        preset.likes += 1
        preset.save()

        total_likes = preset.likes.count()
        return JsonResponse({'success': True, 'total_likes': total_likes})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

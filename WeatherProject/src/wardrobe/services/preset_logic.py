import json

from django.http import JsonResponse

from src.wardrobe.models import Preset


def save_preset(request):
    if request.method == 'POST':
        owner = request.user
        clothes_dict = request.POST.get('clothes_list')
        preset_name = request.POST.get('preset_name')

        if clothes_dict and preset_name:
            Preset.objects.create(owner=owner, clothes_dict=clothes_dict, name=preset_name)
            return JsonResponse({'status_code': 200, 'message': 'Success'})
        else:
            return JsonResponse({'status_code': 400, 'message': 'Invalid data received'})
    else:
        return JsonResponse({'status_code': 405, 'message': 'Method Not Allowed'})

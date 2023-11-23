from django.http import HttpResponse
from src.wardrobe.models import Preset


def save_preset(request):
    if request.method == 'POST':
        owner = request.user
        clothes_dict = request.POST.get('clothes_list')
        preset_name = request.POST.get('preset_name')
        Preset.objects.create(owner=owner, clothes_dict=clothes_dict, name = preset_name )
        return HttpResponse('Шаблон успешно сохранен')
    else:
        return HttpResponse('Недопустимый метод запроса')



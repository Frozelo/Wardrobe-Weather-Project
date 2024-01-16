from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from src.wardrobe.models import Preset


def likes_logic(preset_id):
    try:
        preset = get_object_or_404(Preset, id=preset_id)
        preset.likes += 1
        preset.save()

        total_likes = preset.likes.count()
        return JsonResponse({'success': True, 'total_likes': total_likes})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

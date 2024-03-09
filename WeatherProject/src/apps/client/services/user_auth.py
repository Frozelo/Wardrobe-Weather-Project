from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect, render

from src.apps.client.models import Client

# TODO Client exist fix with core services
from src.core.services import filter_objects
from src.core.request_service import get_request_params


def get_user_login_params(request):
    try:
        return get_request_params(request, params=('username', 'password'))
    except KeyError as e:
        return JsonResponse({'error': str(e), 'message': 'Missing credentials'}, status=400)


def user_auth_logic(request):
    login_params, error_message = get_user_login_params(request)
    if not login_params:
        return JsonResponse({'error': error_message, 'message': 'Missing credentials'}, status=400)

    user = authenticate(request, **login_params)
    if user is None:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    login(request, user)
    if filter_objects(obj=Client.objects, user=user, exist=True):
        return redirect('profile')
    else:
        return redirect('/profile/settings')

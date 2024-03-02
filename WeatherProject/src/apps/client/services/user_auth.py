from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect, render

from src.apps.client.models import Client

# TODO Client exist fix with core services
from src.core.services import filter_objects


def user_auth_logic(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError as e:
        return JsonResponse({'error': str(e), 'message': 'Missing credentials'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # if Client.objects.filter(user=user).exists():
        if filter_objects(obj=Client.objects,
                          user=user,
                          exist=True):
            print('yes!')
            return redirect('profile')
        else:
            return redirect('/profile/settings')
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

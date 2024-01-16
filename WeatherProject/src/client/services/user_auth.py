from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect


def user_auth_logic(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except KeyError as e:
            return JsonResponse({'error': e, 'message': 'Missing credentials'}, status=400)
        except Exception as e:
            return JsonResponse({'error': e, 'message': 'An error occurred'}, status=500)

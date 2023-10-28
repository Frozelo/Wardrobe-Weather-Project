from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from src.client.forms import AvatarUploadForm
from src.wardrobe.models import group_clothes_by_type


@login_required
def profile(request):
    user = request.user
    clothes_by_type = group_clothes_by_type(user)

    first_name = user.first_name
    last_name = user.last_name
    client = user.client
    region = client.region
    city = client.city
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.client)
        if form.is_valid():
            form.save()
    else:
        form = AvatarUploadForm(instance=client)
    context = {'user': user,
               'name': first_name,
               'last_name': last_name,
               'region': region,
               'city': city,
               'clothes_by_type': clothes_by_type,
               'form': form
               }
    return render(request, 'user/profile.html', context)

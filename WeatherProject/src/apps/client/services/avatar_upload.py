from src.apps.client.forms import AvatarUploadForm


def avatar_upload_form_logic(request, client) -> AvatarUploadForm:
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.client)
        if form.is_valid():
            form.save()
    else:
        form = AvatarUploadForm(instance=client)

    return form

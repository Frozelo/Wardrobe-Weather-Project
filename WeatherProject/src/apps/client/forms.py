from django import forms
from .models import Client

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['avatar']

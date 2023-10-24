from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', editable=False)
    country = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user} - {self.city}"

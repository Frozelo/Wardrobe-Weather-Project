from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', editable=False)
    city = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.user} - {self.city}"
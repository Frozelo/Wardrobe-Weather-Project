from django.db import models


# Create your models here.

class Season(models.Model):
    season_name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.season_name}'

# Generated by Django 4.1.5 on 2024-01-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0006_preset_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='rate',
            field=models.IntegerField(blank=True, choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], null=True),
        ),
    ]

# Generated by Django 4.1.5 on 2024-02-29 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0008_alter_clothes_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='type_of_clothes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_of_clothes', to='wardrobe.typeofclothes'),
        ),
    ]

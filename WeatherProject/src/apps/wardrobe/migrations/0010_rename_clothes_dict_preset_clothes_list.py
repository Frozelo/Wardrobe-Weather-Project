# Generated by Django 4.1.5 on 2024-03-04 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0009_alter_clothes_type_of_clothes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preset',
            old_name='clothes_dict',
            new_name='clothes_list',
        ),
    ]

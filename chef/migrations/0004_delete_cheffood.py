# Generated by Django 4.2.3 on 2023-07-31 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0003_chef_food_cheffood'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChefFood',
        ),
    ]
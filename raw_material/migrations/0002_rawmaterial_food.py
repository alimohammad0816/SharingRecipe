# Generated by Django 4.2.3 on 2023-07-31 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alter_food_raw_materials'),
        ('raw_material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='food',
            field=models.ManyToManyField(to='food.food'),
        ),
    ]

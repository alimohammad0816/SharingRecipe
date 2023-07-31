from django.db import models


class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    amount_of = models.CharField(max_length=255)
    food = models.ManyToManyField('food.Food')

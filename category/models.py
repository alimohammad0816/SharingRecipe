from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    food = models.ManyToManyField('food.Food')


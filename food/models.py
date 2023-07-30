from django.db import models
from raw_material.models import RawMaterial
from category.models import Category


class Food(models.Model):
    class RankChoices(models.TextChoices):
        very_bad_taste = 1, 'very_bad'
        bad_taste = 2, 'bad'
        usual_taste = 3, 'usual'
        yummy_taste = 4, 'yummy'
        delicious_taste = 5, 'delicious'

    raw_materials = models.ManyToManyField(RawMaterial)
    foods_category = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    recipe = models.TextField()
    ranking = models.CharField(choices=RankChoices.choices, null=True, blank=True, max_length=10)



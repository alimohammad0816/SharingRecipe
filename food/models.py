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

    raw_materials = models.ManyToManyField(RawMaterial, related_name='material_of_food')
    foods_category = models.ManyToManyField(Category, related_name='category_of_food')
    chefs_of_food = models.ManyToManyField('chef.Chef', related_query_name='chefs_of_food')
    picture = models.ImageField(upload_to='media/upload/food/', blank=True, null=True)
    name = models.CharField(max_length=100)
    recipe = models.TextField()
    ranking = models.CharField(choices=RankChoices.choices, null=True, blank=True, max_length=10)

    def __str__(self):
        return self.name



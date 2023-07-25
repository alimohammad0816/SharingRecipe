from django.db import models
from django.contrib.auth.models import AbstractUser


class Chef(AbstractUser):
    class RankChoices(models.TextChoices):
        very_bad_taste = 1, 'very_bad'
        bad_taste = 2, 'bad'
        usual_taste = 3, 'usual'
        yummy_taste = 4, 'yummy'
        delicious_taste = 5, 'delicious'

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    rank = models.CharField(choices=RankChoices.choices, null=True, blank=True, max_length=10)

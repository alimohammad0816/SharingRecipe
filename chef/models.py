from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Chef(AbstractUser):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(validators=[
        RegexValidator(
            regex=r"^\S+@\S+\.\S+$",
            message='email is not valid',
        ),
    ])
    password = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
            message='password is not good',
        ),
    ])

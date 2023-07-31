from django.db import models
from django.contrib.auth.models import AbstractUser


class Chef(AbstractUser):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=70, unique=True)
    email_regex = r"^\S+@\S+\.\S+$"
    email = models.EmailField(validators=email_regex)
    password_regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    password = models.CharField(max_length=20, validators=password_regex)

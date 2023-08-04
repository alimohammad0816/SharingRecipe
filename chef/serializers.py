from rest_framework import serializers
from chef.models import *
from django.contrib.auth.hashers import make_password


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password',)

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

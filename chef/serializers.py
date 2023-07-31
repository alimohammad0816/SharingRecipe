from rest_framework import serializers
from chef.models import *


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'food',)

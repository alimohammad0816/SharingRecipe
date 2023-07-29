from rest_framework import serializers
from raw_material.models import *


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ('id', 'name', 'amount_of',)

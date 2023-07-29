from django.contrib import admin
from raw_material.serializers import *


@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount_of']

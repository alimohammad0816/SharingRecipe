from django.contrib import admin
from chef.serializers import *


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'rank']
    list_filter = ['username', 'rank']

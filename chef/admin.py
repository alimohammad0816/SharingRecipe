from django.contrib import admin
from chef.serializers import *


class ChefFoodAdmin(admin.TabularInline):
    model = ChefFood
    extra = 1


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username']
    list_filter = ['username']
    inlines = (ChefFoodAdmin,)

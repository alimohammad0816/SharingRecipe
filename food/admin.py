from django.contrib import admin
from food.models import *


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'recipe', 'ranking']
    list_filter = ['ranking']

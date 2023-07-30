from django.contrib import admin
from food.models import *


class FoodMaterialAdmin(admin.TabularInline):
    model = FoodMaterialMemberShip
    extra = 1


class FoodCategoryAdmin(admin.TabularInline):
    model = FoodCategoryMemberShip
    extra = 1


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'recipe', 'ranking', 'raw_materials', 'food_category']
    list_filter = ['ranking', 'food_category']

    inlines = (FoodMaterialAdmin, FoodCategoryAdmin,)

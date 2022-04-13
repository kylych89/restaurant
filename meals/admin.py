from django.contrib import admin

from meals.models import Category, Meals

# Register your models here.
admin.site.register(Meals)
admin.site.register(Category)
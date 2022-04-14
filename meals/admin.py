from django.contrib import admin
from django.utils.safestring import mark_safe


from meals.models import Category, Meals

# Register your models here.
@admin.register(Meals)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'people',
        'is_speciality',
        'price',
        'preparation_time',
        'image',
        'slug',
    )

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


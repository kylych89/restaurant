from django.contrib import admin
from django.utils.safestring import mark_safe
from abouts.models import AboutUs, WhyChoiceUs, Chef


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'image',
    )

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"



@admin.register(WhyChoiceUs)
class WhyChoiceUsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
    )


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'subtitle',
        'bio',
        'image',
    )

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"


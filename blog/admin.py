from django.contrib import admin
from django.utils.safestring import mark_safe


from blog.models import Category, Post, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'author',
        'image',
        'category',
        'created_date',
        'tags'
    )

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'content',
        'created'
    )

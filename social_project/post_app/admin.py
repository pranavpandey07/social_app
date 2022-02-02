from django.contrib import admin

# Register your models here.
from post_app import models

@admin.register(models.post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_id',
    'post_content',
    'created_by',
    'likes_counts',
    'dislikes_count',
    'shares_count',
    'created_at',
    'updated_at'

    )


   
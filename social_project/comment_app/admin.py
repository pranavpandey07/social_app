from django.contrib import admin

# Register your models here.
from comment_app import models

@admin.register(models.comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_id',
    'comment_content',
    'created_by',
    'post',
    'likes_counts',
    'dislikes_count',
    'created_at',
    'updated_at'

    )



   









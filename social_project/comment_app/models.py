from django.db import models
from user_app.models import user
from post_app.models import post

# Create your models here.
class comment(models.Model):
    comment_id=models.AutoField(blank=False,primary_key = True)
    comment_content=models.CharField(max_length=1000)
    created_by=models.ForeignKey(user,on_delete=models.CASCADE)
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    likes_counts=models.PositiveIntegerField(default=0,null=True)
    dislikes_count=models.PositiveIntegerField(default=0,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_content
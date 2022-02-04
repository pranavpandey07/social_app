from django.db import models
from user_app.models import user

# Create your models here.
class post(models.Model):
    post_id=models.AutoField(blank=False,primary_key = True)
    post_content=models.CharField(max_length=1000)
    created_by=models.ForeignKey(user,on_delete=models.CASCADE)
    views=models.PositiveIntegerField(default=0,null=True)
    likes_counts=models.PositiveIntegerField(default=0,null=True)
    dislikes_count=models.PositiveIntegerField(default=0,null=True)
    shares_count=models.PositiveIntegerField(default=0,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_content
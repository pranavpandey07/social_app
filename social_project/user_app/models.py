from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.PositiveIntegerField(blank=False,primary_key = True,auto_created = True)
    first_name=models.CharField(blank=False,max_length=20)
    last_name=models.CharField(blank=False,max_length=20)
    mobile_num=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name +self.last_name
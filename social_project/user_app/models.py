from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.
class user(AbstractUser):
    user_id=models.AutoField(blank=False,primary_key = True)
    username=models.CharField(blank=True,max_length=100)
    first_name=models.CharField(blank=False,max_length=20)
    last_name=models.CharField(blank=False,max_length=20)
    mobile_num=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','mobile_num','address','state','country','zip_code']
    #objects = CustomUserManager()

    def __str__(self):
        return self.email
from django.contrib import admin

# Register your models here.
from user_app import models

@admin.register(models.user)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
    'first_name',
    'last_name',
    'mobile_num',
    'email',
    'password',
    'address',
    'state',
    'country',
    'zip_code',
    'created_at',
    'updated_at'
       

    )

    


   

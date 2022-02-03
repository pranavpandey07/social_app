from rest_framework import serializers
from user_app import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.user
        fields="__all__"
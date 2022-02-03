from rest_framework import serializers
from post_app import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.post
        fields="__all__"
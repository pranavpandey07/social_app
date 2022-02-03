from rest_framework import serializers
from comment_app import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.comment
        fields="__all__"

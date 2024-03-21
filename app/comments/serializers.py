from rest_framework import serializers
from .models import Comment
from users.serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'like', 'dislike','user', 'created_at', 'updated_at']
from rest_framework import serializers
from .models import Video
from users.serializer import UserSerializer

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Video
        fields = "__all__"
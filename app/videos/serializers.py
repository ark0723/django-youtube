from rest_framework import serializers
from .models import Video
from users.serializer import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):
    # user: video = 1: N
    user = UserSerializer(read_only = True)
    # commentS: video = N: 1 -> reverse process 필요 -> _set을 붙이면 부모에 속한 자녀들을 모두 찾을 수 있다
    # 여러개의 댓글 가능
    # comment_set = CommentSerializer(read_only = True, many= True)

    class Meta:
        model = Video
        fields = '__all__'


class VideoDetailSerializer(serializers.ModelSerializer):
    # user: video = 1: N
    user = UserSerializer(read_only = True)
    # commentS: video = N: 1 -> reverse process 필요 -> _set을 붙이면 부모에 속한 자녀들을 모두 찾을 수 있다
    # 여러개의 댓글 가능
    comment_set = CommentSerializer(read_only = True, many= True)

    class Meta:
        model = Video
        fields = '__all__'
        depth = 1

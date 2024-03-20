from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import status
# VideoList
# api/v1/video
# GET: 전체 비디오 목록 조회
# post: 새로운 비디오 생성

# request.get()
# request.post()
class VideoList(APIView):
    def get(self, request):
        # QuerySet
        videos = Video.objects.all()
        
        # 시리얼라이저 : object -> json
        serializer = VideoSerializer(videos, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)
        
    def post(self, request):
        data = request.data # json
        serializer = VideoSerializer(data = data) # json -> object

        if serializer.is_valid(): # 유효한 데이터면
            serializer.save(user = request.user) # 데이터를 db에 저장(저장하는 사람이 누구인지: user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        # 유효하지 않다면
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# VideoDetail
# api/v1/video/{video id}
# GET, PUT, DELETE
from rest_framework.exceptions import NotFound

class VideoDetail(APIView):
    def get(self, request, pk): # api/v1/video/{pk}
        try: 
            video = Video.objects.get(pk = pk) # queryset
        except Video.DoesNotExist:
            raise NotFound
        
        serializer = VideoSerializer(video) # obj -> json
        return Response(serializer.data) 

    def put(self, request, pk):
        video = Video.objects.get(pk = pk) # db에서 불러온 데이터
        user_data = request.data # 유저가 보낸 데이터

        serializer = VideoSerializer(video, user_data) # video데이터를 user_data로 변경
        
        serializer.is_valid(raise_exception = True)
        serializer.save() # DB에 업데이트 적용 # is_valid()함수를 먼저 실행해야 save()함수가 실행됨

        return Response(serializer.data)

    def delete(self, request, pk):
        video = Video.objects.get(pk = pk)
        video.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
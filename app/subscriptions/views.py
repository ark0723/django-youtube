from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Subscription
from .serializers import SubSerializer
# SubscriptionList
# post: 구독하기

class SubscriptionList(APIView):
    def get(self, request):
        # 내가(로그인한 사용자) 구독하고 있는 유투버 리스트
        subs = Subscription.objects.filter(subscriber = request.user)
        serializer = SubSerializer(subs, many = True)
        return Response(serializer.data)

    def post(self, request):
        # 유저가  보내는 데이터(json)
        user_data = request.data
        serializer = SubSerializer(data = user_data) # json -> object

        serializer.is_valid(raise_exception = True)
        serializer.save(subscriber = request.user) # 구독하는 사람은 나야

        return Response(serializer.data, 201)


# subscriptionDetail
# get: 특정 유저의 구독자 리스트 조회
# delete: 구독 취소
class SubsriptionDetail(APIView):
    def get(self, request, pk):
        # api/v1/sub/{pk} -> pk = 1번 유저가 구독한 사람들의 리스트를 불러오겠다
        subs = Subscription.objects.filter(subscribed_to = pk) 
        serializer = SubSerializer(subs, many = True)

        return Response(serializer.data)

    def delete(self, request, pk):

        # 현재 로그인한 유저만 삭제할수 있도록 subscriber = request.suer 추가
        sub = get_object_or_404(Subscription, pk = pk, subscriber = request.user)
        sub.delete()
        
        return Response(status = status.HTTP_204_NO_CONTENT)

        
from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse
from rest_framework import status
from .models import Subscription

# todo: 내가 구독하고 있는 유투버 리스트 추가
# [GET] : pk = 나 자신, pk입력받을 필요 없음
# 대댓글

class SubscriptionTestCase(APITestCase):
    def get():
        # todo: 내가 구독하고 있는 유투버 리스트 추가
        # [GET] : pk = 나 자신, pk입력받을 필요 없음
        pass 
    def setUp(self):
        #테스트 코드 실행전 가장 먼저 실행됨
        # 데이터 생성
        # 2명의 유저 생성
        self.user1 = User.objects.create_user(email = 'test1@gmail.com', password = 'pw123')
        self.user2 = User.objects.create_user(email = 'test2@gmail.com', password = 'pw123')
        # 한명 유저 로그인
        self.client.login(email = 'test1@gmail.com', password = 'pw123')

    def test_sub_list_post(self):
        # 구독하기 테스트
        url = reverse('sub-list')
        # 내가 user2를 구독한다.
        data = {
            'subscribed_to':self.user2.pk,
            'subscriber': self.user1.pk 
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, 201) # 201: created
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_sub_detail_get(self):
        # 특정 유저의 구독자 리스트 조회

        # user1이 user2를 구독
        Subscription.objects.create(subscriber = self.user1, subscribed_to = self.user2)
        # api/v1/sub/<pk>
        url = reverse('sub-detail', kwargs={'pk':self.user2.pk})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1) # 2번 유저를 구독한 구독자 수가 1이면 ok
        self.assertTrue(len(res.data) > 0) # 2번 유저를 구독한 구독자 수가 1이면 ok
  
    def test_sub_detail_delete(self):
        # user1이 user2를 구독
        sub = Subscription.objects.create(subscriber = self.user1, subscribed_to = self.user2)
        # 구독취소
        # api/v1/sub/<pk>/
        url = reverse('sub-detail', kwargs={'pk':sub.id})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0) # 테스트 함수내에서 생성한 DB국한됨

# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'
# docker-compose run --rm app sh -c 'python manage.py test subscriptions'
# docker-compose run --rm app sh -c 'flake8'
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb # python debugger

class VideoAPITestCase(APITestCase):
    # setUp: 테스트가 실행되기전 동작하는 함수
    # 데이터를 생성해준다: (1) 유저생성/로그인 -> (2) 비디오 생성
    def setUp(self):
        # 유저생성
        self.user = User.objects.create_user(
            email = 'mobbom@naver.com',
            password = 'password123'
        )

        # 유저로그인
        self.client.login(email = 'mobbom@naver.com', password = 'password123')

        # 비디오 생성
        self.video = Video.objects.create(
            title = 'test video',
            link = 'http://www.test.com',
            user = self.user
        )
    # 127.0.0.1:8000/api/v1/video
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v1/video'
        url = reverse('video-list') # urls.py의 name으로부터 가져옴
        res = self.client.get(url) # 전체 비디오 조회 데이터를 받아옴

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertTrue(len(res.data) > 0)

        # title column(required로 설정했다면)이 res data에 들어있는지
        for video in res.data:
            self.assertIn('title', video)


    def test_video_list_post(self):
        url = reverse('video-list') # urls.py의 name으로부터 가져옴

        data = {
            'title': 'test video2',
            'link': 'http://test.com',
            'category': 'test category',
            'thumbnail':'http://test.com',
            'video_uploaded_url': 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b"file_content", 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.post(url, data)
        # pdb.set_trace()
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')
    
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk': self.video.pk})
        data = {
            'title': 'updated video2',
            'link': 'http://test.com',
            'category': 'test category',
            'thumbnail':'http://test.com',
            'video_uploaded_url': 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b"file_content", 'video/mp4'),
            'user': self.user.pk
        }
        
        res = self.client.put(url, data) # 서버에 요청 ->  response 서버로부터 받는다
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video2')
    
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk': self.video.pk})

        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        # 지워졌는지 다시 확인
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
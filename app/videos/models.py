from django.db import models
from common.models import CommonModel
from users.models import User

class Video(CommonModel):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # 이미지는 s3 bucket저장 -> url받아서 db에 저장
    video_uploaded_url = models.URLField()
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법
    user = models.ForeignKey(User, on_delete=models.CASCADE)

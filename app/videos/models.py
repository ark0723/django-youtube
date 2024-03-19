from django.db import models
from common import CommonModel
from users.models import User

class Video(CommonModel):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_uploaded_url = models.URLField()
    video_file = models.FileField(upload_to='videos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.

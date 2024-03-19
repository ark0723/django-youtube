from django.db import models

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True) # 처음 생성될때만 시간생성
    updated_at = models.DateTimeField(auto_now = True) # 데이터 변경될때마다 시간 업데이트

    class Meta:
        abstract = True # DB에 테이블을 추가하지 말아줘
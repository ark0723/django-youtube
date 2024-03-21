from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Subscription(CommonModel):
    # 나 : 나를 구독하는 사람 (1: N)
    subscribed_to = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'subscribers')
    # 나: 내가 구독하는 사람 (1: N)
    subscriber = models.ForeignKey(User, on_delete = models.CASCADE, related_name ='subscriptions' )


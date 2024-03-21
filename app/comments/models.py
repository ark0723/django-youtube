from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default = 0)
    dislike = models.PositiveIntegerField(default = 0)
    # user: comment = 1: N
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # video: comment = 1: N
    video = models.ForeignKey(Video, on_delete = models.CASCADE)


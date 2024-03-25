from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

class Reaction(CommonModel):
    
    # user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '') -> circular import error발생 확률 높음
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete = models.CASCADE)
    # reacton (like, dislike, cancel) -> choice
    LIKE = 1 # 상수변수(대문자로 쓰는게 룰)
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    reaction = models.IntegerField(
        choices = REACTION_CHOICES,
        default = NO_REACTION
    )
    
    # 전역함수
    @staticmethod # ORM depth2 모델.objects.get, filter().aggregate() # sql joins query
    def get_video_reaction(video):
        # 예: 1번 비디오 - 좋아요/싫어요/무반응 다 가져와
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter = Q(reaction = Reaction.LIKE)),
            dislikes_count = Count('pk', filter = Q(reaction = Reaction.DISLIKE))
        )

        return reactions


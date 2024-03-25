from django.db import models
from common.models import CommonModel


# chat room  나눈 이유: 이점
# 관리용이
# 확장성 (오픈채팅방, 업무채팅방 -비밀번호 입력해야 들어갈수 있다)
class ChatRoom(CommonModel):
    name = models.CharField(max_length = 100)

class ChatMessage(CommonModel):
    # User:Msg = 1: N
    # 사용자가 계정을 탈퇴해도 해당 메시지는 남기고 싶다 : 정보통신법 3개월 채팅 보관 
    # -> 알수없음으로 뜨게 하려면: SET_NULL, null = True(해당 필들에서 null값이 가능)
    sender = models.ForeignKey('users.User', on_delete = models.SET_NULL, null = True)
    message = models.TextField()
    # 어떤 방에서 주고받은 메시지인지
    # room: msg = 1: N
    room = models.ForeignKey(ChatRoom, on_delete = models.CASCADE) # 채팅방이 사라지면 메시지도 사라진다



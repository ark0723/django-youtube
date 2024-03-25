from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatRoom, ChatMessage
from .serializer import ChatRoomSerializer,ChatMessageSerializer

def chat_html(request): # HTML 연결
    return render(request, 'index.html')

# ChatRoom
## ChatRoomLISt : api/v1/chat : GET(전체 채팅방 조회), POST(채팅방 개설) // AUTH - request.user
## ChatRoomDetail: api/v1/chat/{room_id} : PUT(채팅방 제목 수정, 인원수 제한 등), DELETE(해당 채팅룸 삭제)
class ChatRoomList(APIView):
    # api/v1/chat/room
    def get(self, request):
        rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(rooms, many = True)
        return Response(serializer.data) # 200
    def post(self, request):
        user_data = request.data # 유저가 보내준 데이터 
        serializer = ChatRoomSerializer(data = user_data) # 객체로 만든다

        serializer.is_valid(raise_exception = True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.erors)
        serializer.save()

# ChatMessage
## ChatMessageList: GET (채팅방의 채팅 내역 조회), POST(채팅 메시지 생성)
class ChatMessageList(APIView):
    # api/v1/chat/{room_id}/messages
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id = room_id)
        msgs = ChatMessage.objects.filter(room = chatroom)
        # 직렬화
        serializer = ChatMessageSerializer(msgs, many = True)
        return Response(serializer.data)
        
    def post(self, request, room_id):
        user_data = request.data
        # chatroom이 존재하는지 체크
        chatroom = get_object_or_404(ChatRoom, id = room_id)

        serializer = ChatMessageSerializer(data = user_data)
        serializer.is_valid(raise_exception = True)
        serializer.save(room = chatroom, sender = request.user) # FK: room, sender

        return Response(serializer.data, 201)


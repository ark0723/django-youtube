# 비동기
from channels.generic.websocket import  AsyncWebsocketConsumer
import json

# consumer class: websocket 연결처리 
# 코파일럿
# channel layer - group(socket으로 연결)
# async - await
class ChatConsumer( AsyncWebsocketConsumer):
    # 소켓 연결
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_'+ str(self.room_id)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    # 데이터 통로: 양방향 데이터 실시간 소통
    async def receive(self, text_data):
        # data: 그룹으로 보내는 데이터

        data_json = json.loads(text_data)
        message = data_json.get('message')

        await self.channel_layer.group_send(self.room_group_name, {
            'type':'chat_message',
            'message': message
        })

    async def chat_message(self, event):
        msg = event['message']
        # email = event['email']

        await self.send(text_data = json.dumps({
            'type':'chat.message',
            'message':msg,
            # 'email': email
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
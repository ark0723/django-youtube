# channels library 활용해서 socket  연결하는 비동기 라우트 구현
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    'http': get_asgi_application,
    'websocket':AuthMiddlewareStack(
        URLRouter(websocker_urlpatterns) # ws://127.0.0.1:8000/ws/{room_id}
    )
})
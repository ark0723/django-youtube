from django.contrib import admin
from .models import ChatRoom, ChatMessage

# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    pass

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass
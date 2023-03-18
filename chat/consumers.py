import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Calls


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        completed_service = await self.verify_connect()
        if completed_service:
            self.disconnect("sem permissão")
            self.close("Sem permissão")
            return

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, msg_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = self.user
        message = text_data_json["message"]

        await self.save_message(message, user)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message",
                                   "message": message,
                                   f"user": f"{user}"}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,
                                              "user": user}))

    @database_sync_to_async
    def save_message(self, text_data, user):
        call = Calls.objects.filter(title_group_name=self.room_name).first()

        messages = call.messages
        last_id = messages[-1]["id"] if messages else 0

        messages.append(
            {
                "id": last_id+1,
                "owner": f"{user}",
                "message": text_data
            }
        )
        call.messages = messages
        call.save()

    @database_sync_to_async
    def verify_connect(self):
        calls_filter = Calls.objects.filter(
            title_group_name=self.room_name).exists()
        self.call_db = Calls.objects.filter(
            title_group_name=self.room_name).first()
        self.user = self.scope['user']
        return not calls_filter or self.call_db.completed_service or not any([self.user == self.call_db.sender, self.user == self.call_db.attendant])

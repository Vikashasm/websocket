from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MyConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        self.room_name='test_consumer'
        self.group_name='test_consumer_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'message':'you are connected'}))


    def receive(self, text_data=None, bytes_data=None):
       self.send(text_data=json.dumps(text_data))
       
    def disconnect(self, close_code):
       print('disconnected')

    def send_notification(self,event):
        print('send notification')
        self.send(text_data=json.dumps({'payload':event.get('value')}))
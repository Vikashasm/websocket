import json
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your models here.
class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    chat=models.CharField(max_length=700)
    is_seen=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.chat

    def save(self,*args,**kwargs):
        print('hello')
        channel_layer=get_channel_layer()
        data={
            'message':self.chat
        }
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group',{
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )

        return super(Notification,self).save(*args,**kwargs)
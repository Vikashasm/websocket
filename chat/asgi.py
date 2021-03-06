"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.urls import path
from app import consumers
import django


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

application = get_asgi_application()

ws_patterns=[
    path('ws/test/',consumers.MyConsumer.as_asgi())
]
 
application=ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
import os

import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import info.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CollegeERP.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            info.routing.websocket_urlpatterns
        )
    ),
})
from django.urls import path, re_path

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

from game.consumers import GameConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
            path(r'game/<int:game_id>/<username>', GameConsumer),
        ]),
})

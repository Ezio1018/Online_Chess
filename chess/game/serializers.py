

from rest_framework.serializers import Serializer
from rest_framework import serializers

class GameInfoSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    owner_id = serializers.CharField()
    owner_side= serializers.CharField()
    owner_online = serializers.BooleanField()
    time = serializers.CharField()
    CHOICES=(
        (1,"等待对手"),
        (2,"游戏开始"),
        (3,"游戏结束"))
    status = serializers.ChoiceField(choices=CHOICES,source="get_status_display")

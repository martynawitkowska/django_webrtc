from rest_framework import serializers

from users.serializers import CustomUserSerializer
from . import models


class TopicSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = models.Topic
        fields = ["id", "user", "name", "description", "date_created"]


class StageSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = models.Stage
        fields = ["topic", "name", "description"]

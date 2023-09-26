from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import CustomUserSerializer
from . import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id', 'name', 'created_at']


class ParticipantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = models.Participant
        fields = ['id', 'user', 'joined_at', 'room']

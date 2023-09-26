from rest_framework import serializers

from . import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id', 'name', 'created_at']


class ParticipantSerializer(serializers.ModelSerializer):
    # user = CustomUserSerializer()

    class Meta:
        model = models.Participant
        fields = ['id', 'user', 'joined_at', 'room']
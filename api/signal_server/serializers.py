from rest_framework import serializers

from users.serializers import CustomUserSerializer
from . import models
from .models import Offer, Answer, IceCandidate


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id', 'name', 'created_at']


class ParticipantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = models.Participant
        fields = ['id', 'user', 'joined_at', 'room']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'caller', 'target', 'sdp', 'timestamp']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'caller', 'target', 'sdp', 'timestamp']


class IceCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCandidate
        fields = ['id', 'participant', 'target', 'candidate', 'sdp_mid', 'sdp_mline_index', 'timestamp']

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Participant(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name="participants")
    user = models.ForeignKey("users.CustomUser", on_delete=models.DO_NOTHING, related_name="participants")
    joined_at = models.DateTimeField(auto_now_add=True)

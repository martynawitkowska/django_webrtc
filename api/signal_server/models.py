from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Participant(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name="participants")
    user = models.ForeignKey("users.CustomUser", on_delete=models.DO_NOTHING, related_name="participants", null=True)
    joined_at = models.DateTimeField(auto_now_add=True)


class Offer(models.Model):
    caller = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='offers')
    target = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='offer_targets')
    sdp = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    caller = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='answers')
    target = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='answer_targets')
    sdp = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class IceCandidate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='ice_candidates')
    target = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='ice_candidate_targets')
    candidate = models.TextField()
    sdp_mid = models.CharField(max_length=255)
    sdp_mline_index = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


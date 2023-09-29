from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="topics", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"Roadmap for {self.name} generated for {self.user.username}"


class Stage(models.Model):
    topic = models.ForeignKey("Topic", related_name="stages", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

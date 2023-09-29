from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class CustomUser(AbstractUser):
    pass


class Avatar(models.Model):
    avatar = models.FileField(upload_to="avatars/")
    owner = models.ForeignKey(get_user_model(), related_name="avatars", on_delete=models.CASCADE)

    def __str__(self):
        return f"Avatar for {self.owner.username}"

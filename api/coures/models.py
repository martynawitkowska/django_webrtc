from django.contrib.auth import get_user_model
from django.db import models


class Course(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name="courses", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey("Category", related_name="courses", on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

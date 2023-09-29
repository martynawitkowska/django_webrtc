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


class Enrollment(models.Model):
    student = models.ForeignKey(get_user_model(), related_name="enrolled_courses", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", related_name="enrolled_students", on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled to {self.course.name} on {self.date_enrolled}"


class Timetable(models.Model):
    course = models.ForeignKey("Course", related_name="class_dates", on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.subject} on {self.date} at {self.time}"

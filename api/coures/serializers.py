from rest_framework import serializers

from users.serializers import CustomUserSerializer
from . import models


class CourseSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    category = serializers.ChoiceField(choices=[])

    class Meta:
        model = models.Course
        fields = ["id", "owner", "name", "description", "category", "start_date", "end_date"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "name", "description"]


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Timetable
        fields = ["id", "course", "subject", "date", "time", "duration"]


class EnrollmentSerializer(serializers.ModelSerializer):
    student = CustomUserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = models.Enrollment
        fields = ["student", "course", "date_enrolled"]
        read_only_fields = ["date_enrolled"]

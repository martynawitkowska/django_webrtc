from django.contrib import admin

from . import models

admin.site.register(models.Course)
admin.site.register(models.Category)
admin.site.register(models.Timetable)
admin.site.register(models.Enrollment)

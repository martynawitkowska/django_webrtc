from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_active", "date_joined")
    ordering = ("username", "date_joined")


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Avatar)

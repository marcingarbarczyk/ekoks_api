from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]
    list_display = [
        "id",
        "email",
        "role",
        "created",
        "modified",
        "is_active",
    ]
    list_filter = ["role"]

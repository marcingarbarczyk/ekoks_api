from django.contrib import admin

from apps.exercise_base.models import Group, Exercise, Media


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created", "modified"]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

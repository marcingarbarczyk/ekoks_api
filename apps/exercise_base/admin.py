from django.contrib import admin

from apps.exercise_base.models import Group, Exercise, Media


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(Media)
class GroupAdmin(admin.ModelAdmin):
    pass

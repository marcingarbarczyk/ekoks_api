from django.contrib import admin

from apps.training.models import Goal, WorkoutDay


@admin.register(WorkoutDay)
class WorkoutDayAdmin(admin.ModelAdmin):
    list_display = ["id", "workout_date", "user"]


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "exercise",
        "workout_day",
        "sets_count",
        "reps_count",
        "additional_weight",
    ]

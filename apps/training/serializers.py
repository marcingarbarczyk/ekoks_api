from rest_framework.serializers import ModelSerializer

from apps.training.models import WorkoutDay, Goal


class WorkoutDaySerializer(ModelSerializer):
    class Meta:
        model = WorkoutDay
        fields = ["id", "workout_date", "user", "created", "modified"]


class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            "exercise",
            "workout_day",
            "reps_count",
            "sets_count",
            "additional_weight",
            "created",
            "modified",
        ]

from rest_framework.viewsets import ModelViewSet

from apps.training.models import WorkoutDay, Goal
from apps.training.serializers import WorkoutDaySerializer, GoalSerializer


class WorkoutDayViewSet(ModelViewSet):
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer


class GoalViewSet(ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

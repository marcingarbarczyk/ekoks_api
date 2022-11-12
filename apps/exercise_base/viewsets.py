from rest_framework.viewsets import ModelViewSet

from apps.exercise_base.models import Group, Exercise, Media
from apps.exercise_base.serializers import (
    ExerciseSerializer,
    GroupSerializer,
    MediaSerializer,
)


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

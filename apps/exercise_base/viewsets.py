from rest_framework.viewsets import ModelViewSet

from apps.exercise_base.models import Group, Exercise, Media
from apps.exercise_base.serializers import (
    ExerciseSerializer,
    GroupSerializer,
    MediaSerializer,
)
from apps.membership.permissions import PermissionPolicyMixin, IsEditor


class ExerciseViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes_per_method = {
        "update": [IsEditor],
        "create": [IsEditor],
    }


class GroupViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes_per_method = {
        "update": [IsEditor],
        "create": [IsEditor],
    }


class MediaViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes_per_method = {
        "update": [IsEditor],
        "create": [IsEditor],
    }

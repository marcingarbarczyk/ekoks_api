from rest_framework.serializers import ModelSerializer

from apps.exercise_base.models import Exercise, Media, Group


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["__all__"]


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ["__all__"]


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ["__all__"]

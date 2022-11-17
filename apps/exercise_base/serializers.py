from rest_framework.serializers import ModelSerializer

from apps.exercise_base.models import Exercise, Media, Group


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "title", "description"]


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ["id", "title", "description"]


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "title", "description"]

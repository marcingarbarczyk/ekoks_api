from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from django.db import models


class Group(TitleDescriptionModel):
    pass


class Exercise(TitleDescriptionModel, TimeStampedModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Media(TitleDescriptionModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    url = models.URLField()

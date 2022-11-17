from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Group(TitleDescriptionModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")


class Exercise(TitleDescriptionModel, TimeStampedModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("exercise")
        verbose_name_plural = _("exercises")


class Media(TitleDescriptionModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("media")

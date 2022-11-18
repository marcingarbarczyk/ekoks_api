from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from apps.exercise_base.models import Exercise

User = get_user_model()


class WorkoutDay(TimeStampedModel):
    workout_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.user.id} {self.workout_date}"

    class Meta:
        verbose_name = _("workout day")
        verbose_name_plural = _("workout days")


class Goal(TimeStampedModel):
    exercise = models.ForeignKey(
        Exercise, on_delete=models.PROTECT, related_name="goals"
    )
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    reps_count = models.IntegerField()
    sets_count = models.IntegerField()
    additional_weight = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"#{self.id} {self.workout_day}"

    class Meta:
        verbose_name = _("goal")
        verbose_name_plural = _("goals")

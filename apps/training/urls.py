from rest_framework.routers import DefaultRouter

from apps.training.viewsets import WorkoutDayViewSet, GoalViewSet

app_name = "training"

router = DefaultRouter()
router.register("workout_day", WorkoutDayViewSet)
router.register("goal", GoalViewSet)

urlpatterns = router.urls

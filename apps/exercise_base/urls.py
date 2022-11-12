from rest_framework.routers import DefaultRouter

from apps.exercise_base.viewsets import MediaViewSet, ExerciseViewSet, GroupViewSet

app_name = "exercise_base"

router = DefaultRouter()
router.register("media", MediaViewSet)
router.register("exercise", ExerciseViewSet)
router.register("group", GroupViewSet)

urlpatterns = router.urls

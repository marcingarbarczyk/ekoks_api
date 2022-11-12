from django.urls.conf import include, path
from .views import LoginView, ActivationUserEmailView, RegisterView

app_name = "membership"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path(
        "activate/<slug:uidb64>/<slug:token>/",
        ActivationUserEmailView.as_view(),
        name="activate",
    ),
]

from django.urls import path, re_path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="E-Koks API",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("membership/", include("membership.urls")),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view_v1.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view_v1.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view_v1.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

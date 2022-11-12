from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("sys-admin/", admin.site.urls),
    path("api/v1/", include("ekoks_api.api")),
]

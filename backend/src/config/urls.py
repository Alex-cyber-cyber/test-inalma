
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health(_):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("src.catalog.urls")),
    path("health/", health),
]

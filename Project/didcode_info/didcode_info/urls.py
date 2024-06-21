from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path("", include("hello.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

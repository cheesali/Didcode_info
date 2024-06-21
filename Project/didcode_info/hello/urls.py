from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index),
    path("about/", about),
    path("contact/", contact),
    path("get_info/<DIDCODE>/", get_didcode_info),
    path("input_didcode_info/", input_didcode_info)
]

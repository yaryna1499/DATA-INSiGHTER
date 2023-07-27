from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *




urlpatterns = [
    path("palette/", PaletteView.as_view(), name="api_palette"),
]

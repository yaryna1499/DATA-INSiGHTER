from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("api_palette_fromurl", api_palette_fromurl, name="api_palette_fromurl")
]

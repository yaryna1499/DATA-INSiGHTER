from django.urls import path
from .views import *

urlpatterns = [
    path("get_palette/", get_palette, name="get_palette"),
    path("palette_upload/", palette_upload, name="palette_upload"),
    path("palette_show/", palette_show, name="palette_show"),
]
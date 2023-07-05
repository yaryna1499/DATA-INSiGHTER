from django.urls import path
from .views import *

urlpatterns = [
    path("text_cutter/", text_cutter, name="text_cutter"),
    path("show_image/", show_image, name="show_image"),
    path("process_image/", process_image, name="process_image"),
]
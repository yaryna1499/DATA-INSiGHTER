from django.urls import path
from .views import *

urlpatterns = [
    path("recommend_system", recommend_system_view, name="recommend_system"),
]
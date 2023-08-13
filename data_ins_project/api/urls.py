from django.urls import path, include
from .views import PaletteView

urlpatterns = [
    path("api_palette/", PaletteView.as_view(), name="api_palette"),
]

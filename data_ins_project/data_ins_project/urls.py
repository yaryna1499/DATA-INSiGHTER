from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('palette_generator.urls')),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)

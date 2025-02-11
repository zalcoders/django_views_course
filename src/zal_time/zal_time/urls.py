from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("current_time.urls")),
]


handler404 = "general.views.handler404"

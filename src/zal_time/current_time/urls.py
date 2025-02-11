from django.urls import path
from current_time.views import home

app_name = "current_time"
urlpatterns = [
    path('', home, name="home"),
]

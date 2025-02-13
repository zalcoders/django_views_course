from django.urls import path
from current_time.views import home, time_api

app_name = "current_time"
urlpatterns = [
    path('', home, name="home"),
    path('api/<path:tz>/', time_api, name="time_api"),
]

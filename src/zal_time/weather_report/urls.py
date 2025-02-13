from django.urls import path
from weather_report.views import get_weather

app_name = "weather_report"
urlpatterns = [
    path('csv', get_weather, name="get_weather"),
]

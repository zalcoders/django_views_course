from contact_us.views import home
from django.urls import path

app_name = "contact_us"
urlpatterns = [
    path('', home, name="home"),
]

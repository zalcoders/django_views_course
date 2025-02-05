from django.urls import path
from main.views import password_generator_view

urlpatterns = [
    path('', password_generator_view),
]

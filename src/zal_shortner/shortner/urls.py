from django.urls import path

from shortner.views import home_page, result, redirect_view, dashboard


app_name = "shortner"
urlpatterns = [
    path('result/', result),
    path('', home_page, name="generate-new-url"),
    path('<short_url_id:pk>/', redirect_view, name="short-url"),
    path('dashboard/<short_url_id:pk>/', dashboard, name="short-url-dashboard"),
]

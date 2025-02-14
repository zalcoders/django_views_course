from django.urls import path
from uploader.views import upload, success, download

app_name = "shortner"
urlpatterns = [
    path('', upload, name="upload"),
    path('success/<uuid:file_uuid>/', success, name="success"),
    path('download/<uuid:file_uuid>', download, name="download"),
]

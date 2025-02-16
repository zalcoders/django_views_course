from django.urls import path
from uploader.views import upload, download, test_view, get_presigned_url

app_name = "uploader"
urlpatterns = [
    path('', upload, name="upload"),
    path('download/<uuid:file_uuid>', download, name="download"),
    path('get_presigned_url/<uuid:file_uuid>', get_presigned_url, name="get_presigned_url"),

    path('test', test_view, name="test"),
]

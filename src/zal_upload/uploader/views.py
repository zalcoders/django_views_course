from django.shortcuts import render
from utils import upload_file_to_s3


def upload(request):
    if request.method == "POST":
        f = request.FILES["my_file"]

        upload_file_to_s3(f, "zalcoders-upload", f.name)

    return render(request, "uploader/upload.html", {})

def success(request, file_uuid):
    return render(request, "uploader/success.html", {})

def download(request, file_uuid):
    return render(request, "uploader/download.html", {})

def test_view(request):
    return render(request, "uploader/test.html", {})

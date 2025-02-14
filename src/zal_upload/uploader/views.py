from django.shortcuts import render


def upload(request):
    return render(request, "uploader/upload.html", {})

def success(request, file_uuid):
    return render(request, "uploader/success.html", {})

def download(request, file_uuid):
    return render(request, "uploader/download.html", {})

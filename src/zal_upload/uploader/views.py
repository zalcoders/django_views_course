from django.shortcuts import render


def upload(request):
    f = request.FILES["my_file"]

    file_path = f"/home/zalcoders/projects/Recording/DjangoViews/tmp/{f.name}"
    with open(file_path, "wb") as destination_file:
        for chunk in f.chunks():
            destination_file.write(chunk)

    return render(request, "uploader/upload.html", {})

def success(request, file_uuid):
    return render(request, "uploader/success.html", {})

def download(request, file_uuid):
    return render(request, "uploader/download.html", {})

def test_view(request):
    return render(request, "uploader/test.html", {})

from django.shortcuts import render
from utils import upload_file_to_s3
from uploader.models import UploaddedFile

from django.conf import settings
from django.shortcuts import get_object_or_404


def upload(request):
    if request.method == "POST":
        f = request.FILES["my_file"]

        status, key, slug = upload_file_to_s3(f, "zalcoders-upload", f.name)

        if status:
            uploadded_file = UploaddedFile(
                file_name=f.name,
                s3_file_key=key,
                size=float(f.size),
                content_type=f.content_type,
                slug=slug,
            )
            uploadded_file.save()

            site_url = settings.SITE_URL

            return render(request, "uploader/success.html", {"file": uploadded_file, "site_url": site_url})

    return render(request, "uploader/upload.html", {})


def download(request, file_uuid):
    uploadded_file = get_object_or_404(UploaddedFile, slug=file_uuid)
    site_url = settings.SITE_URL
    return render(request, "uploader/download.html", {"file": uploadded_file, "site_url": site_url})


def test_view(request):
    return render(request, "uploader/test.html", {})

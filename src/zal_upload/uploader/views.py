from django.shortcuts import render
from utils import upload_file_to_s3, generate_presigned_url, generate_put_presigned_url
from uploader.models import UploaddedFile

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.urls import reverse

SECONDS_IN_DAYS = 24 * 60 * 60

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

@require_http_methods(["POST"])
def upload_ajax(request):
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

        return JsonResponse({"status": "OK", "success_page_url": ""})


def download(request, file_uuid):
    uploadded_file = get_object_or_404(UploaddedFile, slug=file_uuid)
    if (timezone.now() - uploadded_file.created_at).total_seconds() > SECONDS_IN_DAYS:
        raise Http404("File not found")
    site_url = settings.SITE_URL
    return render(request, "uploader/download.html", {"file": uploadded_file, "site_url": site_url})


def test_view(request):
    return render(request, "uploader/test.html", {})


@require_http_methods(["POST"])
def get_presigned_url(request, file_uuid):
    uploadded_file = get_object_or_404(UploaddedFile, slug=file_uuid)
    url = generate_presigned_url("zalcoders-upload", uploadded_file.s3_file_key)
    return JsonResponse({"url": url})

@require_http_methods(["POST"])
def create_put_presigned_url(request):
    raw_data = request.body
    data = json.loads(raw_data.decode('utf8'))
    file_name = data["name"]
    file_size = float(data["size"])
    content_type = data["content_type"]

    url, slug, s3_file_key = generate_put_presigned_url("zalcoders-upload", file_name, content_type)

    uploadded_file = UploaddedFile(
        file_name=file_name,
        s3_file_key=s3_file_key,
        size=file_size,
        content_type=content_type,
        slug=slug,
    )
    uploadded_file.save()

    download_url = reverse("uploader:download", args=(slug, ))

    return JsonResponse({"url": url, "download_url": download_url})

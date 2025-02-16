from django.db import models
from uuid import uuid4


class UploaddedFile(models.Model):
    file_name = models.CharField("File Name", max_length=256)
    s3_file_key = models.CharField("S3 File KEY", max_length=512)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    uploader_ip = models.CharField("Uploader IP", null=True, max_length=50)
    size = models.FloatField("File Size")
    content_type = models.CharField("Content Type", max_length=50)
    slug = models.CharField("Slug", max_length=50, default=None, blank=True, null=True)

from django.db import models
from django.utils import timezone
from datetime import timedelta
from utils import human_readable_time_diff
from django.conf import settings
from django.urls import reverse


class UploaddedFile(models.Model):
    file_name = models.CharField("File Name", max_length=256)
    s3_file_key = models.CharField("S3 File KEY", max_length=512)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    uploader_ip = models.CharField("Uploader IP", null=True, max_length=50)
    size = models.FloatField("File Size")
    content_type = models.CharField("Content Type", max_length=50)
    slug = models.CharField("Slug", max_length=50, default=None, blank=True, null=True)
    short_url = models.CharField("Short URL", null=True, blank=True, max_length=256)

    @property
    def get_size_str(self):
        size = self.size / 1000
        if size < 1024:
            return "%.2f KB" % size
        elif size >= 1024:
            size = size / 1024
            return "%.2f MB" % size
        
    @property
    def uploaded_at_str(self):
        now = timezone.now()
        diff = now - self.created_at
        total_seconds = diff.total_seconds()

        return human_readable_time_diff(total_seconds)

        
        
    @property
    def url_expiration_remaining_time(self):
        expiration_time = self.created_at + timedelta(days=1)
        diff = expiration_time - timezone.now()
        total_seconds = diff.total_seconds()

        return human_readable_time_diff(total_seconds)
    
    @property
    def final_url(self):
        if self.short_url:
            return self.short_url
        
        return f"{ settings.SITE_URL }{ reverse("uploader:download", args=(self.slug,)) }"

from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

from utils import generate_shortened_url_from_number


class ShortenedURL(models.Model):
    main_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True, max_length=40, default=uuid.uuid4)
    total_clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to="url_qr_codes/", blank=True, null=True)

    def save(self, *args, **kwargs):
        creating = self._state.adding

        super().save(*args, **kwargs)

        if creating:
            # Generate Slug Based on ID
            self.slug = generate_shortened_url_from_number(self.id)
            self.save(update_fields=['slug'])

            # Generate QR Code
            qr = qrcode.make(self.slug)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            self.qr_code.save(f'qr_{self.slug}.png', ContentFile(buffer.getvalue()), save=False)

            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.main_url} ({self.slug})"

from django.contrib import admin
from django.urls import path, register_converter, include

from django.conf.urls.static import static
from django.conf import settings

from url_converters import ShortenedUrlSlugConverter


register_converter(ShortenedUrlSlugConverter, "short_url_id")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("shortner.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

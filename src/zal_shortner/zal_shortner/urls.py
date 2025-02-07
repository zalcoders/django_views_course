from django.contrib import admin
from django.urls import path, register_converter

from django.conf.urls.static import static
from django.conf import settings

from shortner import views as shortner_views
from url_converters import ShortenedUrlSlugConverter


register_converter(ShortenedUrlSlugConverter, "short_url_id")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('result', shortner_views.result),

    path('', shortner_views.home_page),

    path('<short_url_id:pk>', shortner_views.redirect_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

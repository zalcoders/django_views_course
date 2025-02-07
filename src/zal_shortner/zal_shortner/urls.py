from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from shortner import views as shortner_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', shortner_views.home_page),
    path('result', shortner_views.result),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

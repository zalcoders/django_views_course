from django.contrib import admin
from shortner.models import ShortenedURL, PageVisit

admin.site.register(ShortenedURL)
admin.site.register(PageVisit)

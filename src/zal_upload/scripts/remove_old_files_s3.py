import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zal_upload.settings")

import django
django.setup()

from uploader.models import UploaddedFile

all = UploaddedFile.objects.all()

print(all)
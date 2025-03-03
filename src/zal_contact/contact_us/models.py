from django.db import models
from zal_contact.file_storage import MyStorage

class ContactRequest(models.Model):
    name = models.CharField(max_length=50)
    gamer_tag = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    attachment = models.FileField(null=True, blank=True, storage=MyStorage(location="attachements/"))
    message = models.TextField()

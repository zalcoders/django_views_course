from django.conf import settings
from django.core.files.storage import Storage

import boto3

class MyStorage(Storage):
    def __init__(self, base_url=None, location=None):
        self.location = location
        self.client = boto3.client(
            "s3",
            endpoint_url=settings.S3_URL,
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY,
        )

    def _open(self, name, mode="rb"):
        pass

    def _save(self, name, content):
        key = self.location + name
        response = self.client.put_object(Body=content, Bucket=settings.S3_BUCKET_NAME, Key=key)
        return key

    def exists(self, name):
        key = self.location + name
        try:
            self.client.head_object(Bucket=settings.S3_BUCKET_NAME, Key=key)
        except Exception as e:
            return False
        return True
    
    def delete(self, name):
        response = self.client.delete_object(Bucket=settings.S3_BUCKET_NAME, Key=name)

    def url(self, name):
        return f"https://zal-contact.storage.c2.liara.space/{name}"
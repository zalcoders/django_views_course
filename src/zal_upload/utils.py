import boto3
from botocore.exceptions import ClientError
from django.conf import settings


def upload_file_to_s3(f, bucket, key):
    # Upload the file
    s3_client = boto3.client(
        "s3",
        endpoint_url=settings.S3_URL,
        aws_access_key_id=settings.S3_ACCESS_KEY,
        aws_secret_access_key=settings.S3_SECRET_KEY,
    )
    try:
        response = s3_client.put_object(Body=f, Bucket=bucket, Key=key)
    except ClientError as e:
        return False
    return True

import boto3
from botocore.exceptions import ClientError
import datetime as dt

import os
import pytz


S3_URL = os.environ.get("S3_URL", "https://storage.c2.liara.space")

S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY", "1fdgs0o86pbdgtvv")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY", "2699e820-9cad-42ac-96a9-4485ea20da17")


SECONDS_IN_DAYS = 24 * 60 * 60


def list_expired_files_s3(bucket, life_time=SECONDS_IN_DAYS*2):
    s3_client = boto3.client(
        "s3",
        endpoint_url=S3_URL,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
    )

    expiration_date = dt.datetime.now() - dt.timedelta(seconds=life_time)

    paginator = s3_client.get_paginator("list_objects_v2")

    expired_files = []
    for page in paginator.paginate(Bucket=bucket, PaginationConfig={'PageSize': 50}):
        if "Contents" in page:
            for obj in page["Contents"]:
                if obj["LastModified"] < expiration_date.replace(tzinfo=pytz.UTC):
                    expired_files.append(obj["Key"])

    return expired_files


def remove_expired_files_s3(bucket, keys):
    s3_client = boto3.client(
        "s3",
        endpoint_url=S3_URL,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
    )

    for key in keys:
        response = s3_client.delete_object(Bucket=bucket, Key=key)


expired_files = list_expired_files_s3("zalcoders-upload")
print(len(expired_files))
remove_expired_files_s3("zalcoders-upload", expired_files)
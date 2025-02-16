import boto3
from botocore.exceptions import ClientError
from django.conf import settings

from uuid import uuid4


SECONDS_IN_DAYS = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_FIVE_MINUTES = 5 * 60


def upload_file_to_s3(f, bucket, key):
    # Upload the file
    s3_client = boto3.client(
        "s3",
        endpoint_url=settings.S3_URL,
        aws_access_key_id=settings.S3_ACCESS_KEY,
        aws_secret_access_key=settings.S3_SECRET_KEY,
    )
    try:
        file_uuid = uuid4()
        key = f"{file_uuid}/{key}"
        response = s3_client.put_object(
            Body=f, Bucket=bucket, Key=key
        )
    except ClientError as e:
        return False, None, file_uuid
    return True, key, file_uuid


def human_readable_time_diff(total_seconds):
    if total_seconds > SECONDS_IN_DAYS:
        days = int(total_seconds / SECONDS_IN_DAYS)
        return f"{days} Days"
    elif total_seconds > SECONDS_IN_HOUR:
        hours = int(total_seconds / SECONDS_IN_HOUR)
        return f"{hours} Hours"
    elif total_seconds < SECONDS_IN_FIVE_MINUTES:
        return "Recently"
    else:
        minutes = int(total_seconds / 60)
        return f"{minutes} Minutes"

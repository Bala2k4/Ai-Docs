import boto3
from app.config import settings

s3 = boto3.client(
    "s3",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

def upload_to_s3(file, filename):
    s3.upload_fileobj(
        file,
        settings.S3_BUCKET,
        filename,
        ExtraArgs={"ContentType": "application/octet-stream"}
    )

    return f"https://{settings.S3_BUCKET}.s3.{settings.AWS_REGION}.amazonaws.com/{filename}"
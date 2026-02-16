"""
Helper script to package and upload model artifact to S3 for SageMaker.
This is a convenience helper — it does not create endpoints automatically.
Fill AWS creds in environment or use an AWS profile.
"""
import os
import argparse
import boto3
from botocore.exceptions import ClientError


def upload_file(s3_client, file_path, bucket, key):
    s3_client.upload_file(file_path, bucket, key)


def main():
    parser = argparse.ArgumentParser(description="Upload model artifact to S3 for SageMaker")
    parser.add_argument("--model-file", required=True, help="Local model file to upload (e.g. yolov8n.pt)")
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--key", required=True, help="S3 key (path) to upload to")
    args = parser.parse_args()

    s3 = boto3.client("s3")
    try:
        print(f"Uploading {args.model_file} to s3://{args.bucket}/{args.key}")
        upload_file(s3, args.model_file, args.bucket, args.key)
        print("Upload successful. On SageMaker: create a Model from this artifact and deploy an endpoint.")
    except ClientError as e:
        print("Upload failed:", e)


if __name__ == "__main__":
    main()

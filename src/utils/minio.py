import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from minio import Minio

dotenv_path = Path("./config/minio.env")
load_dotenv(dotenv_path)

ACCESS_KEY = os.getenv("MINIO_ROOT_USER")
SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD")
ENDPOINT = os.getenv("MINIO_ENDPOINT")

BUCKET_BRONZE = os.getenv("BUCKET_BRONZE", "bronze")
BUCKET_SILVER = os.getenv("BUCKET_SILVER", "silver")
BUCKET_GOLD = os.getenv("BUCKET_GOLD", "gold")


def get_client() -> Minio:
    return Minio(
        endpoint=ENDPOINT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False
    )


def make_buckeks(logger: logging.Logger) -> None:
    try:
        logger.info("Attempting to connect to the MinIO service.")
        client: Minio = get_client()
        logger.info("Connecting to the MinIO service.")

        logger.info("Attempting to create buckets.")
        for bucket_name in [BUCKET_BRONZE, BUCKET_SILVER, BUCKET_GOLD]:
            if not client.bucket_exists(bucket_name=bucket_name):
                client.make_bucket(bucket_name=bucket_name)
                logger.info(f"Bucket created : {bucket_name}")
            else:
                logger.info(f"Bucket {bucket_name} already exists.")
    except Exception as e:
        logger.error(f" Error MinIO make buckets: {e}.")

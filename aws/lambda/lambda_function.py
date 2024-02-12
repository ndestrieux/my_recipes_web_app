import json
from io import BytesIO

import boto3
from PIL import Image

s3_client = boto3.client("s3")


def create_thumbnail(input_file, output_file):
    with Image.open(input_file) as img:
        thumbnail_size = 300
        left, top, right, bottom = 0, 0, thumbnail_size, thumbnail_size
        if img.width > img.height:
            output_size = (img.width, thumbnail_size)
            img.thumbnail(output_size, Image.LANCZOS)
            left_right_crop = int((img.width - thumbnail_size) / 2)
            left = left_right_crop
            right = img.width - left_right_crop
            img = img.crop((left, top, right, bottom))
        elif img.width < img.height:
            output_size = (thumbnail_size, img.height)
            img.thumbnail(output_size, Image.LANCZOS)
            top_bottom_crop = int((img.height - thumbnail_size) / 2)
            top = top_bottom_crop
            bottom = img.height - top_bottom_crop
            img = img.crop((left, top, right, bottom))
        else:
            output_size = (thumbnail_size, thumbnail_size)
            img.thumbnail(output_size, Image.LANCZOS)
        img.save(output_file, format="JPEG")


def lambda_handler(event, context):
    try:
        s3_bucket_name = event["s3_bucket_name"]
        s3_file_name = event["s3_file_name"]
        media_folder = event["media_folder"]
        thumbnail_folder = event["thumbnail_folder"]
        thumbnail_url = f"{thumbnail_folder}/{s3_file_name.split('/')[-1]}"
        download_path = f"{media_folder}/{s3_file_name}"
        upload_path = f"{media_folder}/{thumbnail_url}"
        buffer_img = BytesIO()
        buffer_thumbnail = BytesIO()
        s3_client.download_fileobj(s3_bucket_name, download_path, buffer_img)
        create_thumbnail(buffer_img, buffer_thumbnail)
        buffer_thumbnail.seek(0)
        s3_client.upload_fileobj(buffer_thumbnail, s3_bucket_name, upload_path)
        return {"statusCode": 200, "body": thumbnail_url}
    except Exception as err:
        return {"statusCode": 500, "body": json.dumps(str(err))}

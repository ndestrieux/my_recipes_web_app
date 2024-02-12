import json

import requests
from django.conf import settings

from app.models import Recipe


def aws_lambda_create_thumbnail(recipe):
    headers = {"Content-Type": "application/json"}
    data = {
        "s3_bucket_name": settings.AWS_STORAGE_BUCKET_NAME,
        "s3_file_name": recipe.image.name,
        "media_folder": settings.MEDIA_LOCATION,
        "thumbnail_folder": Recipe.THUMBNAIL_FOLDER,
    }
    response = requests.post(
        settings.AWS_APIGATEWAY_CREATETHUMBNAIL_URL,
        headers=headers,
        data=json.dumps(data),
    )
    if response.status_code == 200:
        new_thumbnail = response.json().get("body")
        recipe.thumbnail = new_thumbnail
        recipe.save(update_fields=["thumbnail"])

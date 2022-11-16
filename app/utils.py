import os


def rename_image_file(instance, filename):
    ext = filename.split(".")[-1]
    if instance:
        filename = f"{instance.language}_{instance.name}.{ext}"
    return filename

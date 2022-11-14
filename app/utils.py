import os


def rename_image_file(instance, filename):
    upload_to = "images/"
    ext = filename.split(".")[-1]
    if instance:
        filename = f"{instance.language}_{instance.name}.{ext}"
    return os.path.join(upload_to, filename)

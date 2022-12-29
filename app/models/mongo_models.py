from djongo import models as mongo_models

from app.enums import MailTypeChoice


class MailLogs(mongo_models.Model):
    user_id = mongo_models.IntegerField()
    recipient = mongo_models.EmailField()
    recipe_id = mongo_models.IntegerField(blank=True, null=True)
    sent = mongo_models.BooleanField()
    timestamp = mongo_models.DateTimeField(auto_now_add=True)
    type = mongo_models.CharField(
        max_length=32, choices=[(tag.name, tag.value) for tag in MailTypeChoice]
    )

    class Meta:
        ordering = ["-timestamp"]

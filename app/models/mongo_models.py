from djongo import models as mongo_models


class MailLogs(mongo_models.Model):
    from_user_id = mongo_models.IntegerField()
    recipient = mongo_models.CharField(max_length=256)
    recipe_id = mongo_models.IntegerField()
    status = mongo_models.CharField(max_length=256)
    timestamp = mongo_models.DateTimeField(blank=True, null=True)

    class Meta:
        _use_db = "mongodb"
        ordering = ["-timestamp"]

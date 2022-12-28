from djongo import models as mongo_models


class MailLogs(mongo_models.Model):
    from_user_id = mongo_models.IntegerField()
    recipient = mongo_models.EmailField()
    recipe_id = mongo_models.IntegerField()
    sent = mongo_models.BooleanField()
    timestamp = mongo_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

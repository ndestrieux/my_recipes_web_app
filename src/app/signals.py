from asgiref.sync import async_to_sync
from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from app.enums import VoteChoice
from app.models import Ranking, Recipe, VoteHistory
from app.tasks import create_thumbnail
from app.utils.call_aws_apigateway import aws_lambda_create_thumbnail


@receiver(post_save, sender=Recipe)
def create_ranking(sender, instance, created, **kwargs):
    if created:
        Ranking.objects.create(recipe=instance)


@receiver(post_save, sender=VoteHistory)
def update_ranking_on_vote(sender, instance, update_fields, **kwargs):
    ranking = Ranking.objects.get(recipe=instance.recipe)
    if instance.vote == VoteChoice.UP.name:
        ranking.up += 1
        if update_fields:
            ranking.down -= 1
    elif instance.vote == VoteChoice.DOWN.name:
        ranking.down += 1
        if update_fields:
            ranking.up -= 1
    ranking.save()


@receiver(post_delete, sender=VoteHistory)
def update_ranking_on_vote_delete(sender, instance, **kwargs):
    ranking = Ranking.objects.get(recipe=instance.recipe)
    if instance.vote == VoteChoice.UP.name:
        ranking.up -= 1
    elif instance.vote == VoteChoice.DOWN.name:
        ranking.down -= 1
    ranking.save()


@receiver(post_save, sender=Recipe)
def create_alternate_images(sender, instance, created, **kwargs):
    if created and instance.image and instance.image.name != Recipe.DEFAULT_IMAGE:
        if settings.USE_S3:
            aws_lambda_create_thumbnail(instance)
        else:
            create_thumbnail.delay(instance.id).wait()

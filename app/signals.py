from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Ranking, Recipe, VoteHistory
from app.enums import VoteChoice


@receiver(post_save, sender=Recipe)
def create_ranking(sender, instance, created, **kwargs):
    if created:
        Ranking.objects.create(recipe=instance)


@receiver(post_save, sender=VoteHistory)
def update_ranking(sender, instance, created, **kwargs):
    if created:
        ranking = Ranking.objects.get(recipe=instance.recipe)
        if instance.vote == VoteChoice.UP:
            ranking.up += 1
        if instance.vote == VoteChoice.DOWN:
            ranking.down += 1
        ranking.save()
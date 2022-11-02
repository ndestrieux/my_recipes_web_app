from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Ranking, Recipe, VoteHistory


@receiver(post_save, sender=Recipe)
def create_ranking(sender, instance, created, **kwargs):
    print("Signals")
    if created:
        print("Instance created")
        Ranking.objects.create(recipe=instance)

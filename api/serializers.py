from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ModelSerializer

from app.models import VoteHistory, Ranking


class VoteHistorySerializer(ModelSerializer):
    class Meta:
        model = VoteHistory
        fields = [
            "vote",
            "recipe",
        ]

    def create(self, validated_data):
        user = self.context["current_user"]
        recipe = validated_data["recipe"]
        vote = validated_data["vote"]
        user_vote, created = VoteHistory.objects.get_or_create(user=user, recipe=recipe, defaults={"vote": vote})
        if created is False:
            if user_vote.vote == vote:
                user_vote.delete()
            else:
                user_vote.vote = vote
                user_vote.save(update_fields=["vote"])
        return user_vote


class RankingSerializer(ModelSerializer):
    class Meta:
        model = Ranking
        fields = ["pk", "up", "down", ]

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ModelSerializer

from app.models import VoteHistory


class VoteHistorySerializer(ModelSerializer):
    class Meta:
        model = VoteHistory
        fields = [
            "vote",
            "recipe",
            "user",
        ]

    def create(self, validated_data):
        user = validated_data["user"]
        recipe = validated_data["recipe"]
        vote = validated_data["vote"]
        try:
            user_vote = VoteHistory.objects.get(user=user, recipe=recipe)
        except ObjectDoesNotExist:
            user_vote = VoteHistory.objects.create(**validated_data)
        else:
            if user_vote.vote == vote:
                user_vote.delete()
            else:
                user_vote.vote = vote
                user_vote.save(update_fields=["vote"])
        finally:
            return user_vote
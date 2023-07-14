from rest_framework.serializers import (BooleanField, ModelSerializer,
                                        SlugRelatedField)

from app.models import Comment, Ranking, Recipe, VoteHistory


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
        user_vote, created = VoteHistory.objects.get_or_create(
            user=user, recipe=recipe, defaults={"vote": vote}
        )
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
        fields = [
            "pk",
            "up",
            "down",
        ]


class RecipeUpdateFavoritesSerializer(ModelSerializer):
    is_favorited_by = BooleanField()

    class Meta:
        model = Recipe
        fields = [
            "is_favorited_by",
        ]

    def update(self, instance, validated_data):
        user = self.context["current_user"]
        favorite = validated_data["is_favorited_by"]
        if favorite is True:
            instance.is_favorited_by.add(user)
        else:
            instance.is_favorited_by.remove(user)
        instance.save()
        return instance


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "recipe",
            "text",
        ]

    def create(self, validated_data):
        user = self.context["current_user"]
        recipe = validated_data["recipe"]
        text = validated_data["text"]
        comment = Comment.objects.create(user=user, recipe=recipe, text=text)
        return comment


class CommentListSerializer(ModelSerializer):
    user = SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Comment
        fields = "__all__"

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, ListAPIView)

from api.serializers import (CommentCreateSerializer, CommentListSerializer, RankingSerializer,
                             RecipeUpdateFavoritesSerializer,
                             VoteHistorySerializer)
from app.models import Comment, Ranking, Recipe, VoteHistory

# Create your views here.


class VoteHistoryCreateView(LoginRequiredMixin, CreateAPIView):
    model = VoteHistory
    serializer_class = VoteHistorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["current_user"] = self.request.user
        return context


class RankingDetailView(LoginRequiredMixin, RetrieveAPIView):
    model = Ranking
    serializer_class = RankingSerializer
    lookup_field = "pk"
    queryset = Ranking.objects.all()


class RecipeUpdateFavoritesView(LoginRequiredMixin, UpdateAPIView):
    model = Recipe
    serializer_class = RecipeUpdateFavoritesSerializer
    lookup_field = "pk"
    queryset = Recipe.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["current_user"] = self.request.user
        return context


class CommentCreateView(LoginRequiredMixin, CreateAPIView):
    model = Comment
    serializer_class = CommentCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["current_user"] = self.request.user
        return context


class CommentListView(LoginRequiredMixin, ListAPIView):
    model = Comment
    serializer_class = CommentListSerializer

    def get_queryset(self):
        recipe = self.kwargs["recipe"]
        return Comment.objects.filter(recipe=recipe)
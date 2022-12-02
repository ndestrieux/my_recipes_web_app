from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from api.serializers import (CommentSerializer, RankingSerializer,
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
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["current_user"] = self.request.user
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from api.serializers import (RankingSerializer,
                             RecipeUpdateFavoritesSerializer,
                             VoteHistorySerializer)
from app.models import Ranking, Recipe, VoteHistory

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

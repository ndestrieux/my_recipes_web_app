from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from api.serializers import VoteHistorySerializer, RankingSerializer
from app.models import VoteHistory, Ranking

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

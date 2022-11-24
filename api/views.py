from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView

from api.serializers import VoteHistorySerializer
from app.models import VoteHistory

# Create your views here.


class VoteHistoryCreateView(LoginRequiredMixin, CreateAPIView):
    model = VoteHistory
    serializer_class = VoteHistorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["current_user"] = self.request.user
        return context

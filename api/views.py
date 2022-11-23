from rest_framework.generics import CreateAPIView

from api.serializers import VoteHistorySerializer
from app.models import VoteHistory

# Create your views here.


class VoteHistoryCreateView(CreateAPIView):
    model = VoteHistory
    serializer_class = VoteHistorySerializer

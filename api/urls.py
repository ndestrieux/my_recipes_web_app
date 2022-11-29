from django.urls import path

from api.views import RankingDetailView, VoteHistoryCreateView


api_patterns = [
    path("vote/", VoteHistoryCreateView.as_view(), name="vote"),
    path("ranking/<int:pk>/", RankingDetailView.as_view(), name="ranking"),
]
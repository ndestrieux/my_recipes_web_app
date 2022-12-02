from django.urls import path

from api.views import (CommentCreateView, RankingDetailView,
                       RecipeUpdateFavoritesView, VoteHistoryCreateView)

api_patterns = [
    path("vote/", VoteHistoryCreateView.as_view(), name="vote"),
    path("ranking/<int:pk>/", RankingDetailView.as_view(), name="ranking"),
    path(
        "favorites/recipes/<int:pk>",
        RecipeUpdateFavoritesView.as_view(),
        name="favorite",
    ),
    path("comment/", CommentCreateView.as_view(), name="comment"),
]

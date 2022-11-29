from django.contrib.auth.views import LogoutView
from django.urls import path

from app.views import (HomePageView, RecipeCreationView, RecipeDetailView,
                       RecipeListView, UserLoginView, UserRegistrationView)


app_patterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", HomePageView.as_view(), name="home"),
    path("newrecipe/", RecipeCreationView.as_view(), name="add-recipe"),
    path("recipes/", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
]
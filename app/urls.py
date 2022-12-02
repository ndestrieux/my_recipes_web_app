from django.contrib.auth.views import LogoutView
from django.urls import path

from app.views import (FavoriteRecipeListView, HomePageView, MyRecipeListView,
                       RecipeAppetizerListView, RecipeBakeryListView,
                       RecipeBreakfastListView, RecipeCreationView,
                       RecipeDessertListView, RecipeDetailView,
                       RecipeDinnerListView, RecipeDrinkListView,
                       RecipeListView, RecipeLunchListView, UserLoginView,
                       UserRegistrationView)

app_patterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", HomePageView.as_view(), name="home"),
    path("newrecipe/", RecipeCreationView.as_view(), name="add-recipe"),
    path("recipes/", RecipeListView.as_view(), name="recipe-list"),
    path(
        "recipes/breakfast/", RecipeBreakfastListView.as_view(), name="breakfast-list"
    ),
    path("recipes/lunch/", RecipeLunchListView.as_view(), name="lunch-list"),
    path("recipes/dinner/", RecipeDinnerListView.as_view(), name="dinner-list"),
    path("recipes/dessert/", RecipeDessertListView.as_view(), name="dessert-list"),
    path("recipes/drink/", RecipeDrinkListView.as_view(), name="drink-list"),
    path(
        "recipes/appetizer/", RecipeAppetizerListView.as_view(), name="appetizer-list"
    ),
    path("recipes/bakery/", RecipeBakeryListView.as_view(), name="bakery-list"),
    path("recipes/my-recipes/", MyRecipeListView.as_view(), name="my-recipes"),
    path(
        "recipes/favorites/", FavoriteRecipeListView.as_view(), name="favorite-recipes"
    ),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
]

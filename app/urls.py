from django.contrib.auth.views import (LogoutView, PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView)
from django.urls import path

from app.views import (FavoriteRecipeListView, GeneratePdf, HomePageView,
                       MyRecipeListView, PasswordResetRequestView,
                       RecipeAppetizerListView, RecipeBakeryListView,
                       RecipeBreakfastListView, RecipeCreationView,
                       RecipeDessertListView, RecipeDetailView,
                       RecipeDinnerListView, RecipeDrinkListView,
                       RecipeListView, RecipeLunchListView, SendEmailView,
                       UserLoginView, UserRegistrationView)

app_patterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "change_password/",
        PasswordChangeView.as_view(template_name="users/password_change.html"),
        name="password_change",
    ),
    path(
        "change_password/done/",
        PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
        name="password_change_done",
    ),
    path("password_reset", PasswordResetRequestView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
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
    path("recipe/<int:pk>/pdf/", GeneratePdf.as_view(), name="generate-pdf"),
    path("recipe/<int:pk>/send-email/", SendEmailView.as_view(), name="send-email"),
]

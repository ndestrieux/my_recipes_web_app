"""my_recipes_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from api.views import VoteHistoryCreateView
from app.views import UserRegistrationView, UserLoginView, HomePageView, RecipeCreationView, RecipeListView, RecipeDetailView


# router = DefaultRouter()
# router.register("vote", VoteHistoryCreateView, basename="vote")


urlpatterns = [
    path("", RedirectView.as_view(url="home", permanent=False), name="redirect"),
    path("admin/", admin.site.urls),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", HomePageView.as_view(), name="home"),
    path("newrecipe/", RecipeCreationView.as_view(), name="add-recipe"),
    path("recipes/", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("api/vote/", VoteHistoryCreateView.as_view(), name="vote"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from extra_views import CreateWithInlinesView, NamedFormsetsMixin

from app.forms import (IngredientQuantityFormSet, RecipeForm, UserLoginForm,
                       UserRegistrationForm)
from app.models import Ingredient, Recipe, IngredientQuantity


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("register")


class HomePageView(ListView):
    model = Recipe
    template_name = "app/home_page.html"


class RecipeCreationView(LoginRequiredMixin, SuccessMessageMixin, NamedFormsetsMixin, CreateWithInlinesView):
    model = Recipe
    form_class = RecipeForm
    inlines = [
        IngredientQuantityFormSet,
    ]
    inlines_names = [
        "ingredient_forms",
    ]
    template_name = "app/create_recipe.html"
    success_url = reverse_lazy("home")
    success_message = "New recipe \"%(name)s\" has been created successfully"

    def get_context_data(self, **kwargs):
        kwargs["ingredients"] = Ingredient.objects.all()
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["current_user_id"] = self.request.user.id
        return kwargs


class RecipeListView(ListView):
    model = Recipe
    template_name = "app/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe

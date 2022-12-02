from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from extra_views import CreateWithInlinesView, NamedFormsetsMixin

from app.forms import (IngredientQuantityFormSet, RecipeForm, UserLoginForm,
                       UserRegistrationForm)
from app.models import (AppetizerRecipe, BakeryRecipe, BreakfastRecipe,
                        DessertRecipe, DinnerRecipe, DrinkRecipe, Ingredient,
                        LunchRecipe, Recipe, VoteHistory)


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
    queryset = Recipe.objects.all()[:3]

    def get_context_data(self, **kwargs):
        truncate_to = 3
        kwargs["breakfasts"] = BreakfastRecipe.objects.all()[:truncate_to]
        kwargs["lunches"] = LunchRecipe.objects.all()[:truncate_to]
        kwargs["dinners"] = DinnerRecipe.objects.all()[:truncate_to]
        kwargs["desserts"] = DessertRecipe.objects.all()[:truncate_to]
        kwargs["drinks"] = DrinkRecipe.objects.all()[:truncate_to]
        kwargs["appetizers"] = AppetizerRecipe.objects.all()[:truncate_to]
        kwargs["bakeries"] = BakeryRecipe.objects.all()[:truncate_to]
        return super().get_context_data(**kwargs)


class RecipeCreationView(
    LoginRequiredMixin, SuccessMessageMixin, NamedFormsetsMixin, CreateWithInlinesView
):
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
    success_message = 'New recipe "%(name)s" has been created successfully'

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


class MyRecipeListView(LoginRequiredMixin, RecipeListView):
    def get_queryset(self):
        queryset = Recipe.objects.filter(posted_by=self.request.user)
        return queryset


class RecipeBreakfastListView(ListView):
    model = BreakfastRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Breakfasts"
        return super().get_context_data(**kwargs)


class RecipeLunchListView(ListView):
    model = LunchRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Lunches"
        return super().get_context_data(**kwargs)


class RecipeDinnerListView(ListView):
    model = DinnerRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Dinners"
        return super().get_context_data(**kwargs)


class RecipeDessertListView(ListView):
    model = DessertRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Desserts"
        return super().get_context_data(**kwargs)


class RecipeDrinkListView(ListView):
    model = DrinkRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Drinks"
        return super().get_context_data(**kwargs)


class RecipeAppetizerListView(ListView):
    model = AppetizerRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Appetizers"
        return super().get_context_data(**kwargs)


class RecipeBakeryListView(ListView):
    model = BakeryRecipe
    template_name = "app/recipe_category_list.html"

    def get_context_data(self, **kwargs):
        kwargs["list_name"] = "Bakery"
        return super().get_context_data(**kwargs)


class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        is_favorite = current_user in Recipe.objects.get(id=self.object.id).is_favorited_by.all()
        try:
            vote = VoteHistory.objects.get(user=current_user, recipe=self.object)
        except ObjectDoesNotExist:
            vote = None
        kwargs["is_favorite"] = is_favorite
        kwargs["vote"] = vote
        return super().get_context_data(**kwargs)

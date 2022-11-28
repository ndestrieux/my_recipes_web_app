from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, ButtonHolder, Column, Layout, Row, Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from extra_views import InlineFormSetFactory

from app.models import Ingredient, IngredientQuantity, Recipe


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="form-group col-md-6"),
                Column("last_name", css_class="form-group col-md-6"),
                css_class="row",
            ),
            "username",
            "email",
            Row(
                Column("password1", css_class="form-group col-md-6"),
                Column("password2", css_class="form-group col-md-6"),
                css_class="row",
            ),
            ButtonHolder(
                Submit("submit", "register"),
                HTML("<a href='#' class='btn btn-primary'>Cancel</a>"),
            ),
        )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "username",
            "password",
            ButtonHolder(
                Submit("submit", "login"),
                HTML("<a href='#' class='btn btn-primary'>Cancel</a>"),
            ),
        )

        class Meta:
            model = User
            fields = ["username", "password"]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name",
            "content",
            "nb_of_people",
            "image",
            "language",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        self.current_user_id = kwargs.pop("current_user_id")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.posted_by = User.objects.get(pk=self.current_user_id)
        if commit:
            instance.save()
        return instance


class IngredientQuantityForm(forms.ModelForm):
    ingredient = forms.CharField(
        widget=forms.TextInput(attrs={"type": "hidden"}), required=False
    )
    ingredient_value = forms.CharField(
        label="Ingredient", widget=forms.TextInput(attrs={"list": "ingredients"})
    )

    class Meta:
        model = IngredientQuantity
        fields = [
            "ingredient",
            "ingredient_value",
            "quantity",
            "unit",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column(
                    "ingredient",
                    "ingredient_value",
                    HTML(
                        """<datalist id="ingredients">
                            {% for ingredient in ingredients %}
                                <option id="{{ ingredient.id }}" value="{{ ingredient.name }}">
                            {% endfor %}
                        </datalist>"""
                    ),
                    css_class="form-group col-md-4",
                ),
                Column("quantity", css_class="form-group col-md-4"),
                Column("unit", css_class="form-group col-md-4"),
                css_class="row",
            ),
        )

    def clean(self):
        ingredient = self.cleaned_data["ingredient"]
        if ingredient:
            ingredient = Ingredient.objects.get(id=ingredient)
        else:
            ingredient = Ingredient.objects.create(
                name=self.cleaned_data["ingredient_value"]
            )
        self.cleaned_data["ingredient"] = ingredient
        return self.cleaned_data


class IngredientQuantityFormSet(InlineFormSetFactory):
    model = IngredientQuantity
    form_class = IngredientQuantityForm
    factory_kwargs = {"extra": 1, "can_delete": False}

from django.db import models
from django.contrib.auth.models import User

from app.enums import LanguageChoice, VoteChoice


class Recipe(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    nb_of_people = models.IntegerField(blank=False, null=False)
    image = models.ImageField()
    language = models.CharField(
        max_length=32,
        choices=[(tag, tag.value) for tag in LanguageChoice],
        blank=False,
        null=False,
    )
    posted_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.DO_NOTHING
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "language"], name="unique_recipe")
        ]

    def __str__(self):
        return self.name


class Ranking(models.Model):
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    recipe = models.OneToOneField(
        Recipe, blank=False, null=False, on_delete=models.CASCADE
    )


class VoteHistory(models.Model):
    vote = models.CharField(
        max_length=16,
        choices=[(tag, tag.value) for tag in VoteChoice],
        blank=False,
        null=False,
    )
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(
        Recipe, blank=False, null=False, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "recipe"], name="unique_vote")
        ]


class Comment(models.Model):
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(
        Recipe, blank=False, null=False, on_delete=models.CASCADE
    )


class Ingredient(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, unique=True)
    recipes = models.ManyToManyField(
        Recipe, related_name="ingredients", through="IngredientQuantity"
    )

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    unit = models.CharField(max_length=64)

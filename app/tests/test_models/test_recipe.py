from django.test import TestCase

from app.models import Recipe
from app.tests.basesetup import BaseTestSetup


class RecipeModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenRecipeInstanceCreatedInDatabase(self):
        recipes = Recipe.objects.all()
        self.assertIn(self.test_recipe, recipes)

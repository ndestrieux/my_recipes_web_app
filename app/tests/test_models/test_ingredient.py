from django.test import TestCase

from app.models import Ingredient
from app.tests.basesetup import BaseTestSetup


class IngredientModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenIngredientInstanceCreatedInDatabase(self):
        ingredients = Ingredient.objects.all()
        self.assertIn(self.test_ingredient, ingredients)

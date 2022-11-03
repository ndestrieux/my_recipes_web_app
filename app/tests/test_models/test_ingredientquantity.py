from django.test import TestCase

from app.models import IngredientQuantity
from app.tests.basesetup import BaseTestSetup


class IngredientQuantityModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenIngredientQuantityInstanceCreatedInDatabase(self):
        ingredient_recipe_relationships = IngredientQuantity.objects.all()
        self.assertIn(self.test_ingredient_quantity, ingredient_recipe_relationships)

from django.test import TestCase
from django.urls import reverse

from app.tests.basesetup import BaseTestSetup


class RecipeListViewTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenRecipeObjectInListView(self):
        url = reverse("recipe-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_recipe, response.context["recipe_list"])

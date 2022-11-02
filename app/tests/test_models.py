from datetime import datetime as dt

from django.test import TestCase

from app.enums import LanguageChoice, VoteChoice
from app.models import (Comment, Ingredient, IngredientQuantity, Ranking,
                        Recipe, User, VoteHistory)

# Create your tests here.


class BaseTestSetup:
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            password="test",
            email="johndoe@test.com",
        )
        self.test_recipe = Recipe.objects.create(
            name="Applepie",
            content="test",
            nb_of_people=8,
            language=LanguageChoice.EN,
            posted_by=self.test_user,
        )
        self.test_vote = VoteHistory.objects.create(
            vote=VoteChoice.UP,
            user=self.test_user,
            recipe=self.test_recipe,
        )
        self.test_comment = Comment.objects.create(
            text="test",
            date=dt.now(),
            user=self.test_user,
            recipe=self.test_recipe,
        )
        self.test_ingredient = Ingredient.objects.create(name="apple")
        self.test_ingredient_quantity = IngredientQuantity.objects.create(
            ingredient=self.test_ingredient,
            recipe=self.test_recipe,
            quantity=5,
        )

    def tearDown(self) -> None:
        pass


class UserModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenUserInstanceCreatedInDatabase(self):
        users = User.objects.all()
        self.assertIn(self.test_user, users)

    def testShouldReturnValueErrorWhenEmailIsMissing(self):
        with self.assertRaises(TypeError):
            User.objects.create_user(
                first_name="Paul", last_name="Jones", password="test"
            )


class RecipeModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenRecipeInstanceCreatedInDatabase(self):
        recipes = Recipe.objects.all()
        self.assertIn(self.test_recipe, recipes)


class VoteHistoryModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenVoteHistoryInstanceCreatedInDatabase(self):
        votes = VoteHistory.objects.all()
        self.assertIn(self.test_vote, votes)


class CommentModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenCommentInstanceCreatedInDatabase(self):
        comments = Comment.objects.all()
        self.assertIn(self.test_comment, comments)


class IngredientModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenIngredientInstanceCreatedInDatabase(self):
        ingredients = Ingredient.objects.all()
        self.assertIn(self.test_ingredient, ingredients)


class IngredientQuantityModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenIngredientQuantityInstanceCreatedInDatabase(self):
        ingredient_recipe_relationships = IngredientQuantity.objects.all()
        self.assertIn(self.test_ingredient_quantity, ingredient_recipe_relationships)


class RankingModelTest(BaseTestSetup, TestCase):
    def testShouldReturnCreatedRankingInstanceWhenRecipeInstanceIsCreated(self):
        Recipe.objects.create(
            name="test",
            content="test",
            nb_of_people=8,
            language=LanguageChoice.EN,
            posted_by=self.test_user,
        )
        rankings = Ranking.objects.all()
        self.assertGreater(len(rankings), 0)

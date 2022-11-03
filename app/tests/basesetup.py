from datetime import datetime as dt

from django.contrib.auth.models import User

from app.enums import LanguageChoice, VoteChoice
from app.models import (Comment, Ingredient, IngredientQuantity, Recipe,
                        VoteHistory)


class BaseTestSetup:
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="jdoe",
            password="test",
            email="johndoe@test.com",
        )
        self.test_unsatisfied_user = User.objects.create_user(
            first_name="Paul",
            last_name="Jones",
            username="pjones",
            password="test",
            email="pauljones@test.com",
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
        self.test_down_vote = VoteHistory.objects.create(
            vote=VoteChoice.DOWN,
            user=self.test_unsatisfied_user,
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

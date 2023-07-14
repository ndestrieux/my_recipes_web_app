from django.test import TestCase

from app.models import Ranking
from app.tests.basesetup import BaseTestSetup


class RankingModelTest(BaseTestSetup, TestCase):
    def testShouldReturnCreatedRankingInstanceWhenRecipeInstanceIsCreated(self):
        rankings = Ranking.objects.all()
        self.assertGreater(len(rankings), 0)

    def testShouldReturnIncrementedUpFieldWhenUserVotedUp(self):
        ranking = Ranking.objects.get(recipe=self.test_recipe)
        self.assertGreater(ranking.up, 0)

    def testShouldReturnIncrementedDownFieldWhenUserVotedUp(self):
        ranking = Ranking.objects.get(recipe=self.test_recipe)
        self.assertGreater(ranking.down, 0)

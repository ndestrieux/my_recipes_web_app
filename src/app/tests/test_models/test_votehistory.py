from django.test import TestCase

from app.models import VoteHistory
from app.tests.basesetup import BaseTestSetup


class VoteHistoryModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenVoteHistoryInstanceCreatedInDatabase(self):
        votes = VoteHistory.objects.all()
        self.assertIn(self.test_UP_vote, votes)

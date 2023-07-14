from django.test import TestCase

from app.models import Comment
from app.tests.basesetup import BaseTestSetup


class CommentModelTest(BaseTestSetup, TestCase):
    def testShouldReturnTrueWhenCommentInstanceCreatedInDatabase(self):
        comments = Comment.objects.all()
        self.assertIn(self.test_comment, comments)

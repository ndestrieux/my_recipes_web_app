from django.test import TestCase

from app.models import User

# Create your tests here.


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            password="test",
            email="johndoe@test.com",
        )

    def tearDown(self) -> None:
        pass

    def testShouldReturnTrueWhenUserInstanceCreatedInDatabase(self):
        users = User.objects.all()
        self.assertIn(self.test_user, users)

    def testShouldReturnValueErrorWhenEmailIsMissing(self):
        with self.assertRaises(TypeError):
            User.objects.create_user(
                first_name="Paul", last_name="Jones", password="test"
            )

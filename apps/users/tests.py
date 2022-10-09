from django.test import TestCase
from .models import MyUser


class UserPostCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyUser.objects.create_user(
            email="test@gmail.com",
            date_of_birth="1999-01-01",
            password="test123",
        )
        MyUser.objects.create_superuser(
            email="test1@gmail.com",
            date_of_birth="1999-01-01",
            password="test123",
        )

    def test_username_label(self):
        user = MyUser.objects.get(id=1)
        self.assertEqual(user.email, "test@gmail.com")

    def test_user_not_is_staff(self):
        user = MyUser.objects.get(id=1)
        self.assertEqual(user.is_staff, False)

    def test_user_is_admin(self):
        user = MyUser.objects.get(id=2)
        self.assertEqual(user.is_admin, True)

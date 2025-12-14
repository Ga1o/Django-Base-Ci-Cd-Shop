from django.test import TestCase
from .models import UserModel


class UserTest(TestCase):

    def setUp(self):
        # создание тестовйх данных
        UserModel.objects.create(
            user_name='User 1',
            user_email='aa@gmail.com',
            user_phone='89995678333',
            user_password='12345',
            user_created='2025-12-14 14:54:24.515043',
            user_agreed='True',
            user_activated='False',
            user_banned='False',
            last_login='2025-12-14 14:54:24.515043'
        )

    def test_user(self):
        user = UserModel.objects.get(user_name='User 1')
        self.assertEqual(user.user_name, 'User 1')

    def test_user_email(self):
        user = UserModel.objects.get(user_email='aa@gmail.com')
        self.assertEqual(user.user_email, 'aa@gmail.com')

    def test_user_count(self):
        count = UserModel.objects.count()
        self.assertEqual(count, 1)

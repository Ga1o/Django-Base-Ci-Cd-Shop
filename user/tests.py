from django.test import TestCase
from .models import UserModel


class UserTest(TestCase):

    def setUp(self):
        # создание тестовйх данных
        UserModel.objects.create(user_name='User 1')
        UserModel.objects.create(user_name='User 2')

    def test_user(self):
        # тест создания пользователя
        user = UserModel.objects.get(user_name='User 1')
        self.assertEqual(user.user_name, 'User 1')

    def test_user_count(self):
        # тест количества пользователей
        count = UserModel.objects.count()
        self.assertEqual(count, 2)

from .models import UserModel


def get_all_users():
    users = UserModel.objects.all()
    return users

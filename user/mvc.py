from .models import UserModel


def get_all_users():
    users = UserModel.objects.all()
    return users


def get_user_by_id(user_id):
    user = UserModel.objects.get(pk=user_id)
    return user


def get_user_by_email(user_email):
    user = UserModel.objects.get(user_email=user_email)
    return user

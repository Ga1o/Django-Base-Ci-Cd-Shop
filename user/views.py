from django.shortcuts import render
from django.views import View
from .models import UserModel


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')


class ProfileView(View):
    def get(self, request):
        users = UserModel.objects.all()
        data = {
            'users': users
        }
        return render(request, 'user/profile.html', data)

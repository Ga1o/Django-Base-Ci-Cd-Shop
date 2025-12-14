from django.shortcuts import render
from django.views import View
from .mvc import get_all_users


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')


class ProfileView(View):
    def get(self, request):
        users = get_all_users()
        data = {'users': users}
        return render(request, 'user/profile.html', data)

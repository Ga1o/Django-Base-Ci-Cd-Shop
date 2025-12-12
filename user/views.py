from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')


class ProfileView(View):
    def get(self, request):
        return render(request, 'user/profile.html')

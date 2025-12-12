from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class CustomUserModel(admin.ModelAdmin):
    list_display = ('id', 'user_name')
    list_display_links = ('id', 'user_name')

from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class CustomUserModel(admin.ModelAdmin):
    list_display = (
        'id', 'user_name', 'user_email', 'user_phone', 'user_created', 'user_activated', 'user_banned', 'last_login'
    )
    list_display_links = ('id', 'user_name')
    list_per_page = 20

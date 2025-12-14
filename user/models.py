from django.db import models


class UserModel(models.Model):
    user_name = models.CharField('User name', max_length=30)
    user_email = models.EmailField('User Email', unique=True)
    user_phone = models.CharField('User Phone', max_length=20, unique=True)
    user_password = models.CharField('Password', max_length=256)
    user_created = models.DateTimeField('Data created', auto_now_add=True)
    user_agreed = models.BooleanField('Agree', default=False)
    user_activated = models.BooleanField('Activated', default=False)
    user_banned = models.BooleanField('Banned', default=False)
    last_login = models.DateTimeField('Last visit', auto_now=True)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        ordering = ('-user_created',)

    def __str__(self):
        return self.user_name

from django.db import models


class UserModel(models.Model):
    user_name = models.CharField(verbose_name='User name', max_length=30)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user_name

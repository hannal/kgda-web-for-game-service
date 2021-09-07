from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @classmethod
    def find_by_credentials(cls, username, password):
        try:
            user = cls.objects.get(username=username)
        except cls.DoesNotExist:
            return
        if user.check_password(password):
            return user
        return


def default_access_token():
    return uuid4().hex


class AccessToken(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    key = models.CharField(max_length=32, default=default_access_token, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, user: 'User'):
        o = cls(user=user)
        o.save()
        return o

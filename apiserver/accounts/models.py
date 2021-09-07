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

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """Gerenciador de usuários."""

    def create_user(self, username, password=None, **extra_fields):
        """Crie um novo usuário."""
        if not username:
            raise ValueError("É necessário informar o usuário")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """Crie um novo superusuário."""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Modelo de usuário."""

    middle_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Nome do meio")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def _str_(self):
        """Retorne a representação do objeto em string."""
        return self.email


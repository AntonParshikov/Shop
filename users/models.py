from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    user = None

    email = models.EmailField(unique=True, verbose_name='Email')

    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)
    phone_number = models.IntegerField(verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

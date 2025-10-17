from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, verbose_name='Biografía')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')

    def __str__(self):
        return self.username
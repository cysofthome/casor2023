from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to='profile_pictures', null=True, default="avatar.jpg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

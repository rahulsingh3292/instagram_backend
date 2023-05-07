from django.contrib.auth.models import AbstractUser
from django.db import models

from mixins.models import PrimaryKeyMixin, LocationMixin

__all__ = ['User',]

USER_GENDER_CHOICES = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))


class User(AbstractUser, PrimaryKeyMixin, LocationMixin):
    first_name = None
    last_name = None

    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=35)
    bio = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)

    gender = models.CharField(
        max_length=10, choices=USER_GENDER_CHOICES, default='MALE')
    profile_picture = models.FileField(
        upload_to='profile/profile_pictures', blank=True, null=True)

    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = EMAIL_FIELD = ('email')
    REQUIRED_FIELDS = ('username', 'full_name')

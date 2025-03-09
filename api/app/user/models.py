from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    display_name = models.CharField(max_length=64, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"@{self.display_name}" if self.display_name is not None else self.email

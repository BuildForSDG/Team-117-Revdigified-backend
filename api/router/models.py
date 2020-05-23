from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.
class RevDigifiedUser(AbstractBaseUser, PermissionsMixin):
    is_taxpayer = models.BooleanField(default=True)
    is_taxcollector = models.BooleanField(default=False)
    is_auditor = models.BooleanField(default=False)
    is_systemAdmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)
    fist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    DOB = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['DOB','fist_name','last_name' ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

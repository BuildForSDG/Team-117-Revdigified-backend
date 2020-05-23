from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_taxpayer = models.BooleanField(default=True)
    is_taxcollector = models.BooleanField(default=False)
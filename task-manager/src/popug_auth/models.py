from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    REQUIRED_FIELDS = ["uuid"]

    uuid = models.UUIDField(primary_key=False, unique=True)

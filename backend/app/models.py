from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     # Any custom fields you might want to add to the user model
#     pass

# Create your models here.


class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)

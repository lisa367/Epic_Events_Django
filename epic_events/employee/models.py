from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password


class Employee(AbstractBaseUser):
    employee_ref = models.IntegerField
    prenom = models.CharField(max_length=128)
    nom = models.CharField(max_length=128)
    departement = models.CharField(max_length=128)
    role = models.CharField(max_length=250)
    email = models.EmailField()
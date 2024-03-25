from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.apps import apps


class CustomUserManager(UserManager):
    def _create_user(self, prenom, nom, departement, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not prenom or not nom:
            raise ValueError("Vous devez renseigner le prenom et le nom de du collaborateur.")
        if not departement:
            raise ValueError("Le département de l'employé doit être renseigné.")
        # email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        #GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(prenom=prenom, nom=nom, departement=departement, **extra_fields)
        email = f"{prenom}.{nom}@epicevents.com"
        email = self.normalize_email(email)
        user.email = email
        user.employee_ref = str(user.id).zfill(5)
        temp_password = user.employee_ref if "password" not in extra_fields else extra_fields["password"]
        user.password = make_password(temp_password)
        print(user.password)
        user.save(using=self._db)
        return user
    


class Employee(AbstractUser):

    OPTIONS  = [
        ("gestion", "Gestion"),
        ("commercial", "Commercial"),
        ("support", "Support"),
    ]

    employee_ref = models.CharField(max_length=10)
    prenom = models.CharField(max_length=128)
    nom = models.CharField(max_length=128)
    departement = models.CharField(max_length=128, choices=OPTIONS)
    role = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
 

    USERNAME_FIELD = "employee_ref"
    REQUIRED_FIELDS = ["prenom", "nom"]

    objects = CustomUserManager()
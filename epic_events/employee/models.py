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
        user = self.model(prenom=prenom.title(), nom=nom.title(), departement=departement, **extra_fields)
        email = f"{prenom.lower()}.{nom.lower()}@epicevents.com"
        email = self.normalize_email(email)
        user.email = email
        user.employee_ref = str(user.id).zfill(5)
        temp_password = user.employee_ref if "password" not in extra_fields else extra_fields.get("password")
        user.password = make_password(temp_password)
        print(user.password)
        user.save(using=self._db)
        return user
    
    def create_user(self, prenom, nom, departement, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(prenom, nom, departement, **extra_fields)

    def create_superuser(self, prenom, nom, departement, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(prenom, nom, departement, **extra_fields)


class Employee(AbstractUser):

    OPTIONS  = [
        ("Gestion", "Gestion"),
        ("Commercial", "Commercial"),
        ("Support", "Support"),
    ]

    employee_ref = models.CharField(max_length=10)
    prenom = models.CharField(max_length=128)
    nom = models.CharField(max_length=128)
    departement = models.CharField(max_length=128, choices=OPTIONS)
    role = models.CharField(max_length=256, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "employee_ref"
    REQUIRED_FIELDS = ["prenom", "nom", "departement"]

    objects = CustomUserManager()

    def __str__(self):
        return f"Collaborateur : {self.prenom} {self.nom.upper()} - {self.departement.title()}"
    
    def __repr__(self):
        return f"Collaborateur : {self.prenom} {self.nom.upper()} - {self.departement.title()}"


    class Meta:
        verbose_name = "Collaborateur"
        verbose_name_plural = "Collaborateurs"

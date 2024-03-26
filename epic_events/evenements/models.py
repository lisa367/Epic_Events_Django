from django.db import models
from employee.models import Employee
from contrats.models import Contrat


class Evenement(models.Model):
    nom_evenement = models.CharField(max_length=256)
    lieu = models.CharField(max_length=256)
    nom_client = models.CharField()
    email_client = models.EmailField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    nombre_invites = models.IntegerField()
    commentaire = models.TextField()
    contact_support = models.CharField(max_length=128)
    contrat_id = models.ForeignKey(Contrat)
    collaborateur_support_id = models.ForeignKey(Employee)
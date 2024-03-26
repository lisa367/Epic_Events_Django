from django.db import models
from employee.models import Employee
from clients.models import Client


class Contrat(models.Model):
    contact_commercial = models.CharField(max_length=128)
    montant_facture = models.DecimalField()
    montant_redevable = models.DecimalField()
    date_creation = models.DateField()
    statut = models.CharField()
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    collaborateur_id = models.ForeignKey(Employee,)
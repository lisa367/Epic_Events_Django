from django.db import models
from django.contrib.auth import get_user_model

# from employee.models import Employee
from clients.models import Client

Employee = get_user_model()

class Contrat(models.Model):
    CHOIX_STATUT = [
        ("unsigned", "unsigned"),
        ("signed", "signed")
    ]

    contact_commercial = models.CharField(max_length=128)
    montant_facture = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    montant_redevable = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    date_creation = models.DateField()
    statut = models.CharField(max_length=256, choices=CHOIX_STATUT , default="unsigned")
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING, blank=True)
    collaborateur_id = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=1, blank=True)

    def __str__(self) -> str:
        return f"Contrat : n˚{self.id} - client id {self.client_id}"
    
    def __repr__(self) -> str:
        return f"Contrat : n˚{self.id} - client id {self.client_id}"
from django.db import models
from employee.models import Employee


class Client(models.Model):
    nom_complet = models.CharField(max_length=256)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    nom_entreprise = models.CharField(max_length=10)
    date_premier_contact = models.DateField()
    date_dernier_contact = models.DateField()
    contact_commercial = models.CharField(max_length=128)
    collaborateur_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"Client: n˚{self.id} - {self.nom_complet}"
    
    def __repr__(self) -> str:
        return f"Client: n˚{self.id} - {self.nom_complet}"

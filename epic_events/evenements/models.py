from django.db import models
from employee.models import Employee
from contrats.models import Contrat


class Evenement(models.Model):
    nom_evenement = models.CharField(max_length=256)
    lieu = models.CharField(max_length=256)
    nom_client = models.CharField(max_length=256)
    email_client = models.EmailField(blank=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    nombre_invites = models.IntegerField(default=0)
    commentaire = models.TextField(blank=True)
    contact_support = models.CharField(max_length=128, blank=True)
    contrat_id = models.ForeignKey(Contrat, on_delete=models.RESTRICT)
    collaborateur_support_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"Evenement : {self.nom_evenement} ({self.date_debut} - {self.date_fin})"
    
    def __str__(self) -> str:
        return f"Evenement : {self.nom_evenement} ({self.date_debut} - {self.date_fin})"
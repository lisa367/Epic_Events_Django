from django.db import models
from django.contrib.auth import get_user_model

# from employee.models import Employee
from contrats.models import Contrat

Employee = get_user_model()

class Evenement(models.Model):
    nom_evenement = models.CharField(max_length=256, verbose_name="évènement")
    lieu = models.CharField(max_length=256)
    nom_client = models.CharField(max_length=256)
    email_client = models.EmailField(blank=True)
    date_debut = models.DateTimeField(verbose_name="date de début")
    date_fin = models.DateTimeField(verbose_name="date de fin")
    nombre_invites = models.IntegerField(default=0, verbose_name="nombre d'invités")
    commentaire = models.TextField(blank=True)
    contact_support = models.CharField(max_length=128, blank=True)
    contrat_id = models.ForeignKey(Contrat, on_delete=models.DO_NOTHING)
    collaborateur_support_id = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self) -> str:
        return f"Evenement : {self.nom_evenement} ({self.date_debut} - {self.date_fin})"
    
    def __str__(self) -> str:
        return f"Evenement : {self.nom_evenement} ({self.date_debut} - {self.date_fin})"
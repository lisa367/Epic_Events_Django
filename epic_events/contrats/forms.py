from django.forms.models import ModelForm
from .models import Contrat

class ContratForm(ModelForm):
    class Meta:
        model = Contrat
        fields = "__all__"
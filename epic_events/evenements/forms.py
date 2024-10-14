from django.forms.models import ModelForm
from django.forms import DateTimeInput
from .models import Evenement

class EvenementForm(ModelForm):
    class Meta:
        model = Evenement
        fields = "__all__"
        widgets = {"date_debut": DateTimeInput(), "date_fin": DateTimeInput()}
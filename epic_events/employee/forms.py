from django.forms.models import ModelForm

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["prenom", "nom", "departement", "role", "email"]
from django.forms.models import ModelForm
from django.forms import ChoiceField

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["prenom", "nom", "departement", "role", "email"]


class EmployeePasswordForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["password",]
        # widgets = {"role"}
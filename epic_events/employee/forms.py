from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["prenom", "nom", "departement", "role", "photo"]


class EmployeePasswordForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["password",]
        # widgets = {"role"}


class LoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["id", "password"]
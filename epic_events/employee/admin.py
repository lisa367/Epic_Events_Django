from django.contrib import admin
# from backend.settings import AUTH_USER_MODEL
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    fields = ["nom", "prenom", "departement", "role", "photo"]
    #readonly_fields = ("id", "employee_ref")

    def save_form(self, request, form, change=True):
        if not change:
            form.instance = self.model.objects.create_user(
                form.cleaned_data['prenom'],
                form.cleaned_data['nom'],
                form.cleaned_data['departement'],
            )
        return super().save_form(request, form, change)

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)

""" 
{
                    "role" : form.cleaned_data['role'],
                    "photo" : form.cleaned_data['photo'],
                },
"""

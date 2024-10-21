from django.contrib import admin
# from backend.settings import AUTH_USER_MODEL
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    fields = ["nom", "prenom", "departement", "role", "photo"]
    readonly_fields = ("id", "employee_ref", "password")

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)

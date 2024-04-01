from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from models import Employee
from .forms import EmployeeForm, EmployeePasswordForm


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/employees_list.html"
    context_object_name = "employees"


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/create.html"
    form_class = EmployeeForm


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update.html"
    form_class = EmployeeForm


class EmployeePasswordUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update_password.html"
    form_class = EmployeePasswordForm


class EmployeeDeleteView(UpdateView):
    model = Employee
    template_name = "employee/update.html"
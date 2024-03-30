from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/create.html"
    form_class = ''


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update.html"
    form_class = ''


class EmployeePasswordUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update_password.html"
    form_class = ''


class EmployeeDeleteView(UpdateView):
    model = Employee
    template_name = "employee/update.html"
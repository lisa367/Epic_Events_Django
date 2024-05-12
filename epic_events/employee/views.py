from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from evenements.views import upcoming_events, employee_events
from clients.views import employee_clients
from contrats.views import employee_contrats
from models import Employee
from .forms import EmployeeForm, EmployeePasswordForm


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/employees_list.html"
    context_object_name = "employees"


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee/employee_detail.html"
    context_object_name = "employee"


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


# @login_required
def employee_homepage(request):
    context_data = {}
    context_data["next_events"] = upcoming_events()

    employee_data = Employee.objects.get(id=request.user.id)
    context_data["employee_data"] = employee_data

    if employee_data["departement"] == "Commercial" :
        context_data["employee_clients"] = employee_clients(request.user.id)
        context_data["custom_data_1"] = {}
        context_data["employee_contrats"] = employee_contrats(request.user.id)
    elif employee_data["departement"] == "Support" :
        context_data["employee_events"] = employee_events(request.user.id)

    return render(request, "employee/employee_homepage.html", context=context_data)
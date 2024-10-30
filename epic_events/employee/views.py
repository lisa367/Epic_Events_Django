from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from evenements.views import upcoming_events, employee_events, events_without_support
from clients.views import employee_clients
from contrats.views import employee_contrats, contract_without_commercial

from .models import Employee
from .forms import EmployeeForm, EmployeePasswordForm


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/create.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:homepage")


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:homepage")


class EmployeePasswordUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update_password.html"
    form_class = EmployeePasswordForm
    success_url = reverse_lazy("homepage")


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employee/update.html"
    success_url = reverse_lazy("homepage")


class EmployeeDetailView(ListView):
    model = Employee
    template_name = "employee/details.html"
    context_object_name = "employee"
    queryset = Employee.objects.only("id", "employee_ref", "nom", "prenom", "departement", "role", "email")


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/list.html"
    context_object_name = "employees"
    queryset = Employee.objects.only("id", "employee_ref", "nom", "prenom", "departement", "role", "email")[:30]


def new_employee_view(request, *args, **kwargs):
    context = {}
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("valid form")
            form.save()

    else:
        context["form"] = EmployeeForm()
        return render(request, "employee/create.html", context=context)


# @login_required
def employee_homepage(request, *args, **kwargs):
    context_data = {}
    context_data["next_events"] = upcoming_events()

    context_data["employee"] = Employee.objects.filter(id=request.user.id).values()
    # print(request.user.id)
    print(context_data["employee"])
    
    user = context_data["employee"][0]
    context_data["url_1"] = 'employee:homepage'

    """ 
    if user["departement"] == "Commercial" :
        # context_data["employee_clients"] = employee_clients(request.user.id)
        context_data["custom_data_1"] = employee_clients(request.user.id, 5)
        context_data["custom_data_2"] = contract_without_commercial(5)
        context_data["url_1"] = 'clients:my_clients'
        context_data["url_2"] = 'contracts:unassigned'
        # context_data["employee_contrats"] = employee_contrats(request.user.id)

    elif user["departement"] == "Support" :
        # context_data["employee_events"] = employee_events(request.user.id)
        context_data["custom_data_1"] = employee_events(request.user.id, 5)
        context_data["url_1"] = 'evenements:my_events'
        context_data["url_2"] = ''

    elif user["departement"] == "Gestion" :
        context_data["custom_data_1"] = events_without_support(5)
        context_data["custom_data_2"] = contract_without_commercial(5)
        context_data["url_1"] = 'evenements:unassigned'
        context_data["url_2"] = 'contracts:unassigned'
    """
    return render(request, "employee/employee_homepage.html", context=context_data)

# @login_required
def profile_page(request, *args, **kwargs):
    context = {}
    context["employee"] = Employee.objects.filter(id=request.user.id).values()
    #print(context["employee"])
    return render(request, "employee/profile.html", context=context)
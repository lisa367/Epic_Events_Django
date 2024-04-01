from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Client


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client.html'
    context_object_name = "client"


class ClientListView(ListView):
    model = Client
    template_name = "clients/clients_list.html"
    context_object_name = "clients"


class ClientCreateView(CreateView):
    model = Client
    template_name = "clients/create.html"
    form_class = ''


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "clients/update.html"


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "clients/delete.html"


def employee_clients(employee_id):
    filtered_clients = Client.objects.filter(collaborateur_id=employee_id)
    return filtered_clients

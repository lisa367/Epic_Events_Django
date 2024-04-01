from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Contrat


class ClientDetailView(DetailView):
    model = Contrat
    template_name = 'contrats/contrat.html'
    context_object_name = "contrat"


class ClientListView(ListView):
    model = Contrat
    template_name = "contrats/contrats_list.html"
    context_object_name = "contrats"


class ClientCreateView(CreateView):
    model = Contrat
    template_name = "contrats/create.html"
    form_class = ''


class ClientUpdateView(UpdateView):
    model = Contrat
    template_name = "contrats/update.html"


class ClientDeleteView(DeleteView):
    model = Contrat
    template_name = "contrats/delete.html"


def employee_contrats(employee_id):
    filtered_contrats = Contrat.objects.filter(client_id__collaborateur_id=employee_id)
    return filtered_contrats
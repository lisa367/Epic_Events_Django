from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Contrat


class ContratDetailView(DetailView):
    model = Contrat
    template_name = 'contrats/contrat.html'
    context_object_name = "contrat"


class ContratListView(ListView):
    model = Contrat
    template_name = "contrats/contrats_list.html"
    context_object_name = "contrats"


class ContratCreateView(CreateView):
    model = Contrat
    template_name = "contrats/create.html"
    form_class = ''


class ContratUpdateView(UpdateView):
    model = Contrat
    template_name = "contrats/update.html"


class ContratDeleteView(DeleteView):
    model = Contrat
    template_name = "contrats/delete.html"


def employee_contrats(employee_id):
    filtered_contrats = Contrat.objects.filter(client_id__collaborateur_id=employee_id)
    return filtered_contrats
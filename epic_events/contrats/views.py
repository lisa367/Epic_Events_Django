from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from evenements.models import Evenement

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


def employee_contrats(user_id):
    filtered_contrats = Contrat.objects.filter(client_id__collaborateur_id=user_id)
    return filtered_contrats


def contract_without_commercial():
    contracts = Contrat.objects.filter(collaborateur_id=None)
    return contracts


def contract_without_commercial(user_id):
    contracts = Contrat.objects.filter(collaborateur_id=user_id, statut="unsigned")
    return contracts

def unpaid_contracts(user_id):
    filtered_contracts = Contrat.objects.filter(collaborateur_id=user_id,montant_redevable_gt=0)
    return filtered_contracts


def filter_contracts(filters_args):
    filtered_contracts = Contrat.objects.filter(**filters_args)
    return filtered_contracts
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

    def get_queryset(self):
        super().get_queryset()
        clients = Contrat.objects.filter(collaborateur_id=self.request.user.id)

        return clients


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

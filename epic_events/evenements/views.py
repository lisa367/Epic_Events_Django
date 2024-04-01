from datetime import date, datetime as dt
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Evenement

class ClientDetailView(DetailView):
    model = Evenement
    template_name = 'evenements/evenement.html'
    context_object_name = "evenement"


class ClientListView(ListView):
    model = Evenement
    template_name = "evenements/evenements_list.html"
    context_object_name = "evenements"

    def get_queryset(self):
        super().get_queryset()
        clients = Evenement.objects.filter(collaborateur_id=self.request.user.id)

        return clients


class ClientCreateView(CreateView):
    model = Evenement
    template_name = "evenements/create.html"
    form_class = ''


class ClientUpdateView(UpdateView):
    model = Evenement
    template_name = "evenements/update.html"


class ClientDeleteView(DeleteView):
    model = Evenement
    template_name = "evenements/delete.html"


def upcoming_events():
    today = date(dt.now())
    ten_next_events = Evenement.objects.filter(date_debut__gte=today)[:10]
    return ten_next_events
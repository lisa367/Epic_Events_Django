from datetime import date, datetime as dt
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Evenement

class EvenementDetailView(DetailView):
    model = Evenement
    template_name = "evenements/evenement_detail.html"
    context_object_name = "evenement"

class EvenementListView(ListView):
    model = Evenement
    template_name = "evenements/evenements_list.html"
    context_object_name = "evenements"

    def get_queryset(self):
        super().get_queryset()
        clients = Evenement.objects.filter(collaborateur_id=self.request.user.id)

        return clients

def upcoming_events():
    today = dt.now().strftime("%Y-%m-%d")
    ten_next_events = Evenement.objects.filter(date_debut__gte=today).values()[:10]
    return ten_next_events


def employee_events(employee_id, num=-1):
    filtered_events = Evenement.objects.filter(collaborateur_id=employee_id).order_by("-date_debut").values()[:num]
    return filtered_events


def events_without_support(num=-1):
    events = Evenement.objects.filter(collaborateur_support_id=None).values()[:num]
    return events


def generic(request):
    pass
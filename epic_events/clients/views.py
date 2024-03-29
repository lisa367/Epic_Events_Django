from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Client

class ClientDetailView(DetailView):
    model = Client
    template = 'clients/client.html'
    context_object_name = "client"


class ClientListView(ListView):
    model = Client
    template = "clients/clients_list.html"

    def get_queryset(self):
        super().get_queryset()
        clients = Client.objects.filter(collaborateur_id=self.request.user.id)

        return clients
    

def see_all_clients(request):
    all_clients = Client.objects.all()
    return render(request, template_name='', context=all_clients)

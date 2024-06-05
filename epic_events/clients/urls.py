from django.urls import path

from backend.views import AppCreateView, AppUpdateView, AppDeleteView
from .views import ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView
from .models import Client

app_name = "clients"

urlpatterns = [
    # path("new_entry/", ClientCreateView.as_view(), name="new_client"),
    # path("edit_entry/", ClientUpdateView.as_view(), name="edit_client"),
    # path("delete_entry/", ClientDeleteView.as_view(), name="delete_client"),
    path("new_entry/", AppCreateView.as_view(model=Client, title='Nouveau Client', form_class=''), name="new_client"),
    path("edit_entry/", AppUpdateView.as_view(model=Client, title='Modifier un client', form_class=''), name="edit_client"),
    path("delete_entry/", AppDeleteView.as_view(model=Client, title='Supprimer un client', context_object_name="client"), name="delete_client"),
]

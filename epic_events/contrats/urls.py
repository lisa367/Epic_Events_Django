from django.urls import path

from backend.views import AppCreateView, AppUpdateView, AppDeleteView
from .views import ContratDetailView, ContratCreateView, ContratUpdateView ,ContratDeleteView
from .models import Contrat


app_name = "contrats"

urlpatterns = [
    # path("new_entry/", ContratCreateView.as_view(), name="new_contrat"),
    # path("edit_entry/", ContratUpdateView.as_view(), name="edit_contrat"),
    # path("delete_entry/", ContratDeleteView.as_view(), name="delete_contrat"),
    path("new_entry/", AppCreateView.as_view(model=Contrat, title='Nouveau Contrat', form_class=''), name="new_contrat"),
    path("edit_entry/", AppUpdateView.as_view(model=Contrat, title='Modifier un contrat', form_class=''), name="edit_contrat"),
    path("delete_entry/", AppDeleteView.as_view(model=Contrat, title='Supprimer un contrat', context_object_name="contrat"), name="delete_contrat"),
]
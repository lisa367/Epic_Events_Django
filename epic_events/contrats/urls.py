from django.urls import path

from .views import ContratDetailView, ContratCreateView, ContratUpdateView ,ContratDeleteView

app_name = "contrats"

urlpatterns = [
    path("new_entry/", ContratCreateView.as_view(), name="new_contrat"),
    path("edit_entry/", ContratUpdateView.as_view(), name="edit_contrat"),
    path("delete_entry/", ContratDeleteView.as_view(), name="delete_contrat"),
]
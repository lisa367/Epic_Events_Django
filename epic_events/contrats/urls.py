from django.urls import path

from backend.views import AppCreateView, AppUpdateView, AppDeleteView
# from .views import ContratDetailView, ContratCreateView, ContratUpdateView ,ContratDeleteView
from .views import generic
from .models import Contrat
from .forms import ContratForm


app_name = "contrats"

urlpatterns = [
    # path("new_entry/", ContratCreateView.as_view(), name="new_contrat"),
    # path("edit_entry/", ContratUpdateView.as_view(), name="edit_contrat"),
    # path("delete_entry/", ContratDeleteView.as_view(), name="delete_contrat"),
    path("new_entry/", AppCreateView.as_view(model=Contrat, context_object_name="contrat", form_class=ContratForm), name="new_contrat"),
    path("edit_entry/<int:id>", AppUpdateView.as_view(model=Contrat, context_object_name="contrat", form_class=ContratForm), name="edit_contrat"),
    path("delete_entry/<int:id>", AppDeleteView.as_view(model=Contrat, context_object_name="ce contrat"), name="delete_contrat"),
    path("details/<int:id>", generic, name="delete_contracts"),
    path("list/",  generic, name="list_contracts"),
]
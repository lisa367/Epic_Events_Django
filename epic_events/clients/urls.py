from django.urls import path

from .views import ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = "clients"

urlpatterns = [
    path("new_entry/", ClientCreateView.as_view(), name="new_client"),
    path("edit_entry/", ClientUpdateView.as_view(), name="edit_client"),
    path("delete_entry/", ClientDeleteView.as_view(), name="delete_client"),
]

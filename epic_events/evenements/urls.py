from django.urls import path

from .views import EvenementDetailView, EvenementCreateView, EvenementUpdateView, EvenementDeleteView

app_name = "evenements"

urlpatterns = [
    path("new_entry/", EvenementCreateView.as_view(), name="new_event"),
    path("edit_entry/", EvenementUpdateView.as_view(), name="edit_event"),
    path("delete_entry/", EvenementDeleteView.as_view(), name="delete_event"),
]
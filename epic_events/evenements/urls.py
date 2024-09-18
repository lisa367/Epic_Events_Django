from django.urls import path

# from .views import EvenementDetailView, EvenementCreateView, EvenementUpdateView, EvenementDeleteView
from backend.views import AppCreateView, AppUpdateView, AppDeleteView
from .models import Evenement

app_name = "evenements"

urlpatterns = [
    # path("new_entry/", EvenementCreateView.as_view(), name="new_event"),
    # path("edit_entry/", EvenementUpdateView.as_view(), name="edit_event"),
    # path("delete_entry/", EvenementDeleteView.as_view(), name="delete_event"),
    path("new_entry/", AppCreateView.as_view(model=Evenement, context_object_name="évènement", form_class=''), name="new_event"),
    path("edit_entry/", AppUpdateView.as_view(model=Evenement, context_object_name="évènement", form_class=''), name="edit_event"),
    path("delete_entry/", AppDeleteView.as_view(model=Evenement, context_object_name="cet évènement"), name="delete_event"),
]

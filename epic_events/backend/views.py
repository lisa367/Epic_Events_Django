from django.shortcuts import render
from django.forms import Form

from clients.models import Client
from contrats.models import Contrat
from evenements.models import Evenement


# @login_required
def make_queries(request):
    return render(request, "backends/make_queries.html")


class QueryForm(Form):
    TABLE_CHOICE = [
        ("", ""),
    ]
    COLUMN_CHOICE = [
        ("", ""),
    ]
from typing import Any, Mapping
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from django.shortcuts import render
from django import forms

from clients.models import Client
from contrats.models import Contrat
from evenements.models import Evenement


# @login_required
def query_table(request):
    return render(request, "backends/make_queries.html")


class QueryForm(forms.Form):
    """ 
    TABLE_CHOICE = [
        ("", ""),
    ]
    COLUMN_CHOICE = [
        ("", ""),
    ]
     """

    def __init__(self, table_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TABLE_CHOICE = [
            (f"{table_name}", f"{table_name}"),
        ]
        self.COLUMN_CHOICE = [
            (f"{field}", f"{field}") for field in self.TABLE_CHOICE.meta.fields
        ]
        """
        self.COLUMN_CHOICE = [
        (f"{field.name}", f"{field.name}") for field in self.TABLE_CHOICE.meta.get_fields()
    ]
        """

    table = forms.ChoiceField()
    column_name = forms.ChoiceField()

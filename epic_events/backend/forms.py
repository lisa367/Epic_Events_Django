from django import forms

from clients.models import Client
from contrats.models import Contrat
from evenements.models import Evenement



""" 
class TableForm(forms.Form):
    TABLE_CHOICE = [
        (Client, "Clients"),
        (Contrat, "Contrats"),
        (Evenement, "Evenements"),

    ]


class CustomField(forms.Field):
    pass
"""

class QueryForm(forms.Form):
    
    TABLE_CHOICE = [
        (Client, "Clients"),
        (Contrat, "Contrats"),
        (Evenement, "Evenements"),
    ]
   
    COLUMN_CHOICE = [
        ("", ""),
        (f"{field}", f"{field}") for field in TABLE_CHOICE.meta.fields
    ]
    

    def __init__(self, table_name, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.TABLE_CHOICE = [
            (f"{table_name}", f"{table_name}"),
        ]
        self.COLUMN_CHOICE = [
            (f"{field}", f"{field}") for field in self.TABLE_CHOICE.meta.fields
        ]
        self.COLUMN_CHOICE = [
            (f"{field}", f"{field}") for field in table_name.meta.fields
        ]
        """
        self.COLUMN_CHOICE = [
        (f"{field.name}", f"{field.name}") for field in self.TABLE_CHOICE.meta.get_fields()
    ]
        """

    # table = forms.ChoiceField()
    column_name = forms.ChoiceField(choices=COLUMN_CHOICE, label="Colonne")
    column_value = forms.CharField(max_length=256, label="Valeur")


def make_query_form(table_name):
    class QueryForm(forms.Form):
        COLUMN_CHOICE = [
            ("", ""),
            (f"{field}", f"{field}") for field in table_name.meta.fields
        ]

        column_name = forms.ChoiceField(choices=COLUMN_CHOICE, label="Colonne")
        column_value = forms.CharField(max_length=256, label="Valeur")
    
    return QueryForm()


class QueryForm2(forms.Form):
    #
    def __init__(self, table_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.COLUMN_CHOICES = [(f"{field}", f"{field}") for field in table_name.meta.fields]
        self.fields["column_name"] = forms.ChoiceField(choices=self.COLUMN_CHOICES, label="Colonne")
        self.fields["column_value"] = forms.CharField(max_length=256, label="Valeur")
        
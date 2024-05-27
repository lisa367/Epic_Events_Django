from django.shortcuts import render
from django.forms import formset_factory

from .forms import QueryForm, QueryFormSet, make_query_form

# @login_required
def choose_table(request):
    return render(request, "backends/choose_table.html")


# @login_required
def query_table(request, table_name):
    if request.method == "POST":
        TableQueryForm = make_query_form(table_name)
        QueryFormSet = formset_factory(TableQueryForm, absolute_max=10)
    return render(request, "backends/query_table.html")


def logout(request):
    pass
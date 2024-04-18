from django.shortcuts import render
from django.forms import formset_factory

from .forms import QueryForm

# @login_required
def choose_table(request):
    return render(request, "backends/choose_table.html")



# @login_required
def query_table(request, table_name):
    if request.method == "POST":
        QueryFormSet = formset_factory(QueryForm)
    return render(request, "backends/query_table.html")

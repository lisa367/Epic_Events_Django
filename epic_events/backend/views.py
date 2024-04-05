from django.shortcuts import render
from django.forms import Form


# @login_required
def make_queries(request):
    return render(request, "backends/make_queries.html")



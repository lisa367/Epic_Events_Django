from django.shortcuts import render


# @login_required
def make_queries(request):
    return render(request, "backends/make_queries.html")
from typing import Any
from django.shortcuts import render
from django.forms import formset_factory
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import QueryForm, QueryFormSet, make_query_form

def login_user():
    pass

def logout(request):
    logout()


class AppListView(ListView):
    model = ''
    template_name = 'templates/base_list.html'
    context_object_name = ''
    form_class = ''
    title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["object_name"] = self.context_object_name
        return context


class AppCreateView(CreateView, PermissionRequiredMixin):
    model = ''
    template_name = 'templates/base_create.html'
    context_object_name = ''
    form_class = ''
    title = ''
    permission_required = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["object_name"] = self.form_class
        return context


class AppUpdateView(UpdateView, PermissionRequiredMixin):
    model = ''
    template_name = 'templates/base_update.html'
    context_object_name = ''
    form_class = ''
    title = ''
    permission_required = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["form_class"] = self.form_class
        return context
    

class AppDeleteView(DeleteView, PermissionRequiredMixin):
    model = ''
    template_name = 'templates/base_delete.html'
    context_object_name = ''
    title = ''
    permission_required = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["object_name"] = self.context_object_name
        return context


# @login_required
def choose_table(request):
    return render(request, "backends/choose_table.html")


# @login_required
def query_table(request, table_name):
    if request.method == "POST":
        TableQueryForm = make_query_form(table_name)
        QueryFormSet = formset_factory(TableQueryForm, absolute_max=10)
    return render(request, "backends/query_table.html")

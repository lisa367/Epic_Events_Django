"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from .views import query_table, choose_table

urlpatterns = [
    path("/", name="landing-page"),
    path("epic-admin/", admin.site.urls),
    path("employee/", include("employee.urls")),
    path("clients/", include("clients.urls")),
    path("contrats/", include("contrats.urls")),
    path("evenements/", include("evenements.urls")),
    path("queries/", choose_table, name="make-queries"),
]

""" 
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]
"""

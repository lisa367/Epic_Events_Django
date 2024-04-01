from django.urls import path

from .views import employee_homepage, EmployeeDetailView , EmployeePasswordUpdateView

app_name = 'employee'

url_patterns = [
    path("/homepage", employee_homepage, name="homepage" ),
    path("/my_profile", EmployeeDetailView.as_view(), name="profile_page"),
    path("/update_password", EmployeePasswordUpdateView.as_view(), name="update_pwd"),
]
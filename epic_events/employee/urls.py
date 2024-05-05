from django.urls import path

from .views import employee_homepage, EmployeeDetailView , EmployeePasswordUpdateView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

app_name = 'employee'

url_patterns = [
    path("/homepage", employee_homepage, name="homepage" ),
    path("/my_profile", EmployeeDetailView.as_view(), name="profile-page"),
    path("/update_password", EmployeePasswordUpdateView.as_view(), name="update-pwd"),
    path("new_entry/", EmployeeCreateView.as_view(), name="new-client"),
    path("edit_entry/", EmployeeUpdateView.as_view(), name="edit-client"),
]
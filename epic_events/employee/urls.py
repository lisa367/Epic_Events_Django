from django.urls import path

from .views import employee_homepage, profile_page, EmployeePasswordUpdateView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, EmployeeDetailView

app_name = 'employee'

urlpatterns = [
    path("homepage/", employee_homepage, name="homepage" ),
    path("my_profile/", profile_page, name="profile_page"),
    path("update_password/", EmployeePasswordUpdateView.as_view(), name="update_pwd"),
    path("new_entry/", EmployeeCreateView.as_view(), name="new_employee"),
    path("edit_entry/<int:id>", EmployeeUpdateView.as_view(), name="edit_employee"),
    path("delete_entry/<int:id>", EmployeeDeleteView.as_view(), name="delete_employee"),
    path("details/<int:id>", EmployeeDeleteView.as_view(), name="delete_employee"),
    path("list/", EmployeeDeleteView.as_view(), name="delete_employee"),
]
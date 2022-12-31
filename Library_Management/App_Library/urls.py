from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [

    path('add_css_data_coutnry_state_city', add_css_data_coutnry_state_city,name='add_css_data_coutnry_state_city'),
    path('Admin_Login', Admin_Login, name='Admin_Login'),
    path('Admin_logout', Admin_logout, name='Admin_logout'),
    path('Employee_list', Employee_list, name='Employee_list'),
    path('delete_employee_by_admin', delete_employee_by_admin,name='delete_employee_by_admin'),
    path('Dasboard', Dasboard, name='Dasboard'),
    path('student_list', student_list, name='student_list'),
    path('Add_employee_by_admin', Add_employee_by_admin, name='Add_employee_by_admin')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_delete', views.create_delete, name='update_delete'),
    path('employees/<int:employee_id>/', views.employee_details, name='employee_detail'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    
]
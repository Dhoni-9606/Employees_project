from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.employee_detail, name='employee_detail'),
    path('add/', views.add_employee, name='add_employee'),
    path('<int:id>/edit/', views.edit_employee, name='edit_employee'),
]
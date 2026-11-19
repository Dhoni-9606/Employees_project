from django.shortcuts import render,get_object_or_404
from .models import Employee

def employee_detail(request,id):
    # Your view logic here
    employee = get_object_or_404(Employee, id=id)
    context ={
        'employee':employee,
    }
    return render(request, 'employee_detail.html',context)


def add_employee(request):
       return render(request, 'add_employee.html')

# Create your views here.

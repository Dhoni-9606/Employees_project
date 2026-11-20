from django.shortcuts import render,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def employee_detail(request,id):
    # Your view logic here
    employee = get_object_or_404(Employee, id=id)
    context ={
        'employee':employee,
    }
    return render(request, 'employee_detail.html',context)


def add_employee(request):
       if request.method == 'POST':
           form = EmployeeForm(request.POST,request.FILES)
           if form.is_valid():
               form.save()
           else:
                print(form.errors)
       form = EmployeeForm()
       context = {
        'form':form, }
       return render(request, 'add_employee.html',context)


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the employee detail page
    else:
        form = EmployeeForm(instance=employee)
        
    context = {
        'form': form,
        'employee': employee,
    }
    return render(request, 'edit_employee.html', context)


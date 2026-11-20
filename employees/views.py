from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

def employee_detail(request,id):
    # Your view logic here
    employee = get_object_or_404(Employee, id=id)
    context ={
        'employee':employee,
    }
    return render(request, 'employee_detail.html',context)

@login_required
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



def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')  # Redirect to the home page after deletion
        # Redirect to a success page or the employee list page
    context = {
        'employee': employee,
    }
    return render(request, 'delete_employee.html', context)




from django.http import HttpResponse
from employees.models import Employee

def home (request):
    #fetching a data from DB
    employees = Employee.objects.all()
    print(employees)

    return HttpResponse(employees)
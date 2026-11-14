from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    salary=models.IntegerField()
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='employees',blank=True, null=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL,blank=True, null=True, related_name='subordinates')
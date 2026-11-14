from django.contrib import admin

from employees.models import Department, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'designation', 'salary', 'joining_date', 'is_active', 'department', 'manager')
    list_filter = ('is_active', 'department')
    search_fields = ('first_name', 'last_name', 'email', 'designation')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')    

# Register your models here.
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)

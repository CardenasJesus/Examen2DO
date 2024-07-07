from django.contrib import admin

# Register your models here.
from apiexamen import models

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'phone', 'address', 'created', 'updated']


@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created',  'due_date', 'state', 'employee']


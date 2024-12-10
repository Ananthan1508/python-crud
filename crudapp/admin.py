from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin (admin.ModelAdmin):
    list=['Sno','name','Email','phone','Address','password']

admin.site.register (Employee,EmployeeAdmin)

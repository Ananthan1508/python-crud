from django import forms
from .models import Employee
# Create your models here.
class EmployeeForms (forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
       #exclude=['SNo']    any ignor the table






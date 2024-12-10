from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForms
def retrivew_views(request):
    employee = Employee.objects.all()
    return render(request,'crudapp/index.html',{'employee': employee})
def add_views(request):
    form = EmployeeForms()
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrivew_views')
    return render(request,'crudapp/createForms.html',{'form': form})
def delete_views(request,id):
    employee = Employee.objects.get(id=id)
    if request.method=='POST':
        employee.delete()
        return redirect('retrivew_views')
    return render(request,'crudapp/conform_delete.html',{'employee':employee})

def update_views(request,id):
    employee = Employee.objects.get(id=id)
    form= EmployeeForms(instance=employee)
    if request.method == 'POST':
        form = EmployeeForms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('retrivew_views')
    return render(request, 'crudapp/updateForms.html', {'employee': employee,'form': form})






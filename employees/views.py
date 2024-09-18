from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})


def create_delete(request):
    employees = Employee.objects.all()
    return render(request, 'employees/update_delete.html', {'employees': employees})

def employee_details(request,employee_id):
    employee_details = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employees/employee_details.html', {'employee': employee_details })
    


# @login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

# @login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form, 'employee': employee})

# @login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('update_delete')
    return render(request, 'employees/delete_employee.html', {'employee': employee})


def custom_404(request,exception):
    return render(request, '404_NotFound.html')
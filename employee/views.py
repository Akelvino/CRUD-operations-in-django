from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .form import EmployeeCreationForm

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request,'employee/home.html', context)

def add_employee(request):
    form= EmployeeCreationForm()
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'employee/create_employee.html', {'form':form})
from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request,'employee/home.html', context)

def add_employee(request):
    return render(request, 'employee/create_employee.html')
from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee

# Create your views here.
def home(request):
    employee = Employee.objects.all()
    context = {'employee':employee}

    return render(request,'employee/home.html', context)
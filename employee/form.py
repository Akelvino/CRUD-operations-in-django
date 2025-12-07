from django.forms import ModelForm
from .models import Employee

class EmployeeCreationForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
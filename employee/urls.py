from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.add_employee, name='add-employee'),
    path('<int:pk>/employee/', views.edit_employee_details,name='update-information'),
]
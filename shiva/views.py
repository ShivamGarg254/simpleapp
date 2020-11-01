from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def welcome(request):
    return render (request, "welcome.html")

def load_form (request):
    form = EmployeeForm
    return render(request, "index.html ", {'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    employee = Employee.objects.all
    return render(request, 'show.html', {'employee':employee})
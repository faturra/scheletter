from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from integrations.data import dapodik_school, dapodik_users, dapodik_employees, dapodik_students
from .forms import CrispyLoginForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CrispyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CrispyLoginForm()
    
    context = {'form': form}
    return render(request, 'index/index.html', context)

@login_required
def dashboard(request):
    school_info = dapodik_school
    count_emp = len(dapodik_employees)
    count_std = len(dapodik_students)
    context = {'school_info': school_info, 'count_emp': count_emp, 'count_std': count_std}
    return render(request, 'dashboard/dashboard.html', context)

def students(request):
    context = {'students': dapodik_students}
    return render(request, 'reference_data/students/students.html', context)

def employees(request):
    context = {'employees': dapodik_employees}
    return render(request, 'reference_data/employees/employees.html', context)

def graduation(request):
    return render(request, 'reference_data/graduation/graduation.html')

def accounts(request):
    return render(request, 'accounts/employees/accounts.html')

def sign_request(request):
    return render(request, 'administration/sign_request/sign_request.html')

def request_queue(request):
    return render(request, 'administration/request_queue/request_queue.html')

def guest_book(request):
    return render(request, 'administration/guest_book/guest_book.html')

def archives(request):
    return render(request, 'administration/archives/archives.html')

def trash(request):
    return render(request, 'trash/trash.html')
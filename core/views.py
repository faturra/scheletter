from django.shortcuts import render
from integrations.dapodik_api import dapodik_reference

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def dashboard(request):
    count_emp = len(dapodik_reference)
    context = {'employees': dapodik_reference, 'count_emp': count_emp}
    return render(request, 'dashboard/dashboard.html', context)

def students(request):
    return render(request, 'reference_data/students/students.html')

def employees(request):
    context = {'employees': dapodik_reference}
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
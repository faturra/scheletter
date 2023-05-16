from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def students(request):
    return render(request, 'reference_data/students/students.html')

def employees(request):
    return render(request, 'reference_data/employees/employees.html')

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
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def students(request):
    return render(request, 'students/students.html')

def gtk(request):
    return render(request, 'gtk/gtk.html')

def graduation(request):
    return render(request, 'graduation/graduation.html')

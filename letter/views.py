from django.shortcuts import render

# Create your views here.

def letter(request):
    return render(request, 'administration/letter/letter.html')

def student_letter(request):
    return render(request, 'administration/letter/create_letter/student_letter.html')

def employee_letter(request):
    return render(request, 'administration/letter/create_letter/employee_letter.html')
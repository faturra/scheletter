from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StudentsLetterForm

# Create your views here.

@login_required
def letter(request):
    return render(request, 'administration/letter/letter.html')

@login_required
def student_letter(request):
    students_letter_form = StudentsLetterForm()
    context = {'students_letter_form': students_letter_form}

    return render(request, 'administration/letter/create_letter/student_letter.html', context)

@login_required
def employee_letter(request):
    return render(request, 'administration/letter/create_letter/employee_letter.html')

@login_required
def common_letter(request):
    return render(request, 'administration/letter/create_letter/common_letter.html')
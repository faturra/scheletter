from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentsLetterForm

# Create your views here.

@login_required
def letter(request):
    return render(request, 'administration/letter/letter.html')

@login_required
def student_letter(request):
    if request.method == 'POST':
        form = StudentsLetterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'Letter successfully created!')
            return redirect('letter')
    else:
        form = StudentsLetterForm()
    
    context = {'form': form}
    return render(request, 'administration/letter/create_letter/student_letter.html', context)

@login_required
def employee_letter(request):
    return render(request, 'administration/letter/create_letter/employee_letter.html')

@login_required
def common_letter(request):
    return render(request, 'administration/letter/create_letter/common_letter.html')
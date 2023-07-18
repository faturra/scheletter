from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentsLetterForm
from core import decorators, config

# Create your views here.

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def letter(request):
    return render(request, 'administration/letter/letter.html')

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
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
@decorators.group_required(config.hoa, config.scs, config.ecs)
def employee_letter(request):
    return render(request, 'administration/letter/create_letter/employee_letter.html')

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def common_letter(request):
    return render(request, 'administration/letter/create_letter/common_letter.html')
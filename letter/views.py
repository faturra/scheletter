from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentsLetterForm, EmployeesLetterForm
from core import decorators, config
from .models import Students_Letter
from integrations.data import dapodik_students

# Create your views here.

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def letter(request):
    last_letter_number = Students_Letter.objects.order_by('-created_at').first()
    last_number = int(last_letter_number.number.split(' ')[0])

    context = {'last_number': last_number}
    return render(request, 'administration/letter/letter.html', context)

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
    
    student_list = dapodik_students
    
    context = {'form': form, 'student_list': student_list}
    return render(request, 'administration/letter/create_letter/student_letter.html', context)

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def get_student_info(request):
    student_id = request.GET.get('peserta_didik_id')
    try:
        student = next(student for student in dapodik_students if student['peserta_didik_id'] == int(student_id))

        response = {
            'nama_rombel': student['nama_rombel'],
            'tanggal_lahir': student['tanggal_lahir'],
        }
        return JsonResponse(response)
    except StopIteration:
        return JsonResponse({'error': 'Student does not exist'}, status=404)

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def employee_letter(request):
    if request.method == 'POST':
        form = EmployeesLetterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'Letter successfully created!')
            return redirect('letter')
    else:
        form = EmployeesLetterForm()
    
    context = {'form': form}
    return render(request, 'administration/letter/create_letter/employee_letter.html', context)

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def common_letter(request):
    return render(request, 'administration/letter/create_letter/common_letter.html')
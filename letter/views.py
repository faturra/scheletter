from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentsLetterForm, EmployeesLetterForm, CommonLetterForm
from core import decorators, config
from .models import Students_Letter, Employees_Letter, Common_Letter
from integrations.data import dapodik_students

# Create your views here.

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def letter(request):
    latest_student_letter = Students_Letter.objects.order_by('-created_at').first()
    latest_employee_letter = Employees_Letter.objects.order_by('-created_at').first()
    latest_common_letter = Common_Letter.objects.order_by('-created_at').first()

    student_number = int(latest_student_letter.number[:3]) if latest_student_letter else 0
    employee_number = int(latest_employee_letter.number[:3]) if latest_employee_letter else 0
    common_number = int(latest_common_letter.number[:3]) if latest_common_letter else 0

    last_number = max(student_number, employee_number, common_number)

    context = {'last_number': last_number}
    return render(request, 'administration/letter/letter.html', context)


@login_required
@decorators.group_required(config.hoa, config.scs)
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
            messages.error(request, 'Form submission failed. Please check the form.')

    else:
        form = StudentsLetterForm()

    student_list = dapodik_students
    selected_siswa = request.session.get('selected_siswa')
    context = {'form': form, 'student_list': student_list, 'selected_siswa': selected_siswa}
    return render(request, 'administration/letter/create_letter/student_letter.html', context)

@login_required
@decorators.group_required(config.hoa, config.scs)
def sl_selected_siswa(request):
    student_list = dapodik_students

    if request.method == 'POST':
        selected_siswa = request.POST.get('selected_siswa')
        selected_student = next((student for student in student_list if student['nama'] == selected_siswa), None)
        
        if selected_student:
            nama_rombel = selected_student.get('nama_rombel', 'Class not found')
            tempat_lahir = selected_student.get('tempat_lahir', 'Place of birth not found')
            jenis_kelamin = selected_student.get('jenis_kelamin', 'Gender not found')
            tanggal_lahir = selected_student.get('tanggal_lahir', 'Date of birth not found')
            nisn = selected_student.get('nisn', 'NISN not found')
            
            request.session['selected_siswa'] = selected_siswa
            
            return JsonResponse({
                'success': True,
                'nama_rombel': nama_rombel,
                'tempat_lahir': tempat_lahir,
                'jenis_kelamin': jenis_kelamin,
                'tanggal_lahir': tanggal_lahir,
                'nisn': nisn
            })
        else:
            return JsonResponse({'error': 'Nama siswa tidak ditemukan'})
    else:
        return JsonResponse({'error': 'Invalid request method'})



@login_required
@decorators.group_required(config.hoa, config.scs)
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
@decorators.group_required(config.hoa, config.ecs)
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
    if request.method == 'POST':
        form = CommonLetterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'Letter successfully created!')
            return redirect('letter')
    else:
        form = CommonLetterForm()
    
    context = {'form': form}
    return render(request, 'administration/letter/create_letter/common_letter.html', context)
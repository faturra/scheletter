from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentsLetterForm, EmployeesLetterForm, CommonLetterForm
from core import decorators, config
from .models import Students_Letter, Employees_Letter, Common_Letter
# from integrations.data import cache.get('dapodik_students'), cache.get('dapodik_employees')

# Create your views here.

@login_required
@decorators.group_required(config.hoa, config.scs, config.ecs)
def letter(request):
    latest_student_letter = Students_Letter.objects.order_by('-created_at').first()
    latest_employee_letter = Employees_Letter.objects.order_by('-created_at').first()
    latest_common_letter = Common_Letter.objects.order_by('-created_at').first()

    staging_scs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=True).order_by('-created_at')
    count_staging_scs = staging_scs.count()

    staging_ecs = Employees_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=True).order_by('-created_at')
    count_staging_ecs = staging_ecs.count()

    count_staging_hoa = count_staging_scs + count_staging_ecs

    student_number = int(latest_student_letter.number[:3]) if latest_student_letter else 0
    employee_number = int(latest_employee_letter.number[:3]) if latest_employee_letter else 0
    common_number = int(latest_common_letter.number[:3]) if latest_common_letter else 0

    last_number = max(student_number, employee_number, common_number)

    context = {
        'last_number': last_number,
        'count_staging_scs': count_staging_scs,
        'count_staging_ecs': count_staging_ecs,
        'count_staging_hoa': count_staging_hoa,
        }
    return render(request, 'administration/letter/letter.html', context)



@login_required
@decorators.group_required(config.scs)
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

    student_list = cache.get('dapodik_students')
    selected_student = request.session.get('selected_student')
    context = {'form': form, 'student_list': student_list, 'selected_student': selected_student}
    return render(request, 'administration/letter/create_letter/student_letter.html', context)


@login_required
@decorators.group_required(config.scs)
def get_student_info(request):
    student_list = cache.get('dapodik_students')

    if request.method == 'POST':
        selected_student = request.POST.get('selected_student')
        selected_student_next = next((student for student in student_list if student['nama'] == selected_student), None)
        
        if selected_student_next:
            nama_rombel = selected_student_next.get('nama_rombel', 'Class not found')
            tempat_lahir = selected_student_next.get('tempat_lahir', 'Place of birth not found')
            jenis_kelamin = selected_student_next.get('jenis_kelamin', 'Gender not found')
            tanggal_lahir = selected_student_next.get('tanggal_lahir', 'Date of birth not found')
            nisn = selected_student_next.get('nisn', 'NISN not found')
            
            request.session['selected_student'] = selected_student
            
            return JsonResponse({
                'success': True,
                'nama_rombel': nama_rombel,
                'tempat_lahir': tempat_lahir,
                'jenis_kelamin': jenis_kelamin,
                'tanggal_lahir': tanggal_lahir,
                'nisn': nisn
            })
        else:
            return JsonResponse({'error': 'Nama student tidak ditemukan'})
    else:
        return JsonResponse({'error': 'Invalid request method'})



@login_required
@decorators.group_required(config.ecs)
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
@decorators.group_required(config.ecs)
def get_employee_info(request):
    employee_list = cache.get('dapodik_employees')

    if request.method == 'POST':
        selected_employee = request.POST.get('selected_employee')
        selected_employee_next = next((employee for employee in employee_list if employee['nama'] == selected_employee), None)
        
        if selected_employee_next:
            pangkat_golongan_terakhir = selected_employee_next.get('pangkat_golongan_terakhir', 'Rank not found')
            jenis_kelamin = selected_employee_next.get('jenis_kelamin', 'Gender not found')
            tempat_lahir = selected_employee_next.get('tempat_lahir', 'Place of birth not found')
            tanggal_lahir = selected_employee_next.get('tanggal_lahir', 'Date of birth not found')
            nip = selected_employee_next.get('nip', 'NIP not found')
            
            request.session['selected_student'] = selected_employee
            
            return JsonResponse({
                'success': True,
                'pangkat_golongan_terakhir': pangkat_golongan_terakhir,
                'jenis_kelamin': jenis_kelamin,
                'tempat_lahir': tempat_lahir,
                'tanggal_lahir': tanggal_lahir,
                'nip': nip
            })
        else:
            return JsonResponse({'error': 'Employee name not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@login_required
@decorators.group_required(config.scs, config.ecs)
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
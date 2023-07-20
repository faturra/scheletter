import ipinfo
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils import timezone
from integrations.data import dapodik_school, dapodik_employees, dapodik_students
from letter.models import Students_Letter
from core import config
from .decorators import unauthenticated_user, group_required
from .forms import CustomUserCreationForm


# Create your views here.
@unauthenticated_user
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                messages.success(request, 'Sign in success! Hi {}'.format(user.get_full_name()))
                return redirect(next_url)
            else:
                messages.success(request, 'Sign in success! Hi {}'.format(user.get_full_name()))
                return redirect('dashboard')
        else:
            messages.info(request, 'Incorrect email or password')
            return redirect('index')
    return render(request, 'index/index.html')

@login_required
def dashboard(request):
    school_info = dapodik_school
    count_emp = len(dapodik_employees)
    count_std = len(dapodik_students)
    count_ltr = Students_Letter.objects.count()
    count_arc = Students_Letter.objects.count() #+ Employee_Letter.objects.count() + Guest_Book.objects.count()

    count_rs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True).count

    context = {
        'school_info': school_info, 
        'count_emp': count_emp, 
        'count_std': count_std, 
        'count_ltr': count_ltr, 
        'count_arc': count_arc, 
        'count_rs': count_rs
        }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def students(request):
    context = {'students': dapodik_students, 'config': config}
    return render(request, 'reference_data/students/students.html', context)

@login_required
def employees(request):
    context = {'employees': dapodik_employees, 'config': config}
    return render(request, 'reference_data/employees/employees.html', context)

@login_required
@group_required(config.opr)
def accounts(request):
    users =  User.objects.filter(is_superuser=False, is_staff=False)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            
            messages.success(request, 'Account successfully created!')
            return redirect('accounts')
    else:
        form = CustomUserCreationForm()

    context = {'users': users, 'form': form}
    return render(request, 'accounts/employees/accounts.html', context)

@login_required
@group_required(config.opr)
def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()

    messages.success(request, 'Account has been deleted!')
    return redirect('accounts')

@login_required
@group_required(config.opr)
def deactivate_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()

    messages.success(request, 'Account has been deactivated!')
    return redirect('accounts')

@login_required
@group_required(config.opr)
def activate_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()

    messages.success(request, 'Account has been activated!')
    return redirect('accounts')


@login_required
@group_required(config.prl)
def sign_request(request):
    queue = Students_Letter.objects.all()
    digital_sign = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True)
    count_rs = digital_sign.count

    context = {'queue': queue, 'digital_sign': digital_sign, 'count_rs': count_rs}
    return render(request, 'administration/sign_request/sign_request.html', context)

@login_required
@group_required(config.prl)
def check_letter(request, letter_id):
    letter = get_object_or_404(Students_Letter, letter_id=letter_id)
    return render(request, 'administration/sign_request/check_letter/check_letter.html', {'letter': letter})

@login_required
@group_required(config.prl)
def apply_signature(request, letter_id):
    letter = get_object_or_404(Students_Letter, letter_id=letter_id)
    letter.digital_sign_at = timezone.now()
    letter.digital_sign_by = request.user
    letter.digital_sign_job_title = request.user.groups.first().name
    letter.digital_sign_institution = dapodik_school['nama']

    ip_address = request.META.get('REMOTE_ADDR')
    letter.digital_sign_ip = ip_address

    # Mendapatkan informasi lokasi berdasarkan alamat IP pengguna menggunakan ipinfo.io
    handler = ipinfo.getHandler('f2ce563eb2923e')  # Ganti YOUR_IPINFO_API_TOKEN dengan API token Anda
    details = handler.getDetails(ip_address)

    print(details)

    # Periksa jika atribut yang Anda cari ada di dalam objek Details
    if hasattr(details, 'city') and hasattr(details, 'country'):
        location = details.city + ', ' + details.country
        letter.digital_sign_location = location
    else:
        letter.digital_sign_location = 'Unknown'

    messages.success(request, 'Signature applied successfully! Letter has been signed.')
    letter.save()

    return redirect('sign-request')


@login_required
@group_required(config.hoa, config.scs, config.ecs)
def request_queue(request):
    queue = Students_Letter.objects.all()
    digital_sign = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True)
    digital_sign_applied = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=False)
    manual_sign = Students_Letter.objects.filter(type_sign='2')
    count_rs = digital_sign.count

    context = {'queue': queue, 'digital_sign': digital_sign, 'digital_sign_applied': digital_sign_applied, 'manual_sign': manual_sign, 'count_rs': count_rs}
    return render(request, 'administration/request_queue/request_queue.html', context)

@login_required
def guest_book(request):
    return render(request, 'administration/guest_book/guest_book.html')

def guest_and_request_form(request):
    return render(request, 'administration/guest_book/guest_and_request_form/guest_and_request_form.html')

@login_required
def archives(request):
    return render(request, 'administration/archives/archives.html')

@login_required
@group_required(config.hoa)
def trash(request):
    return render(request, 'trash/trash.html')
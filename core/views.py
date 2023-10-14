import ipinfo
import requests
import hashlib
import base64
import time
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.core.cache import cache
from django.template.loader import get_template
from django.utils import timezone
from xhtml2pdf import pisa
# from integrations.data import cache.get('dapodik_school'), cache.get('dapodik_employees'), cache.get('dapodik_students')
from letter.models import Students_Letter, Employees_Letter, Common_Letter
from core import config
from datetime import datetime
from .decorators import unauthenticated_user, group_required
from .forms import StarterForm, AccountsCreationForm, GuestBookForm
from .models import Guest_Book
from PIL import Image


# Create your views here.
@unauthenticated_user
def index(request):
    next_url = request.POST.get('next')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if next_url:
                messages.success(request, 'Welcome, {}'.format(user.get_full_name()))
                return redirect(next_url)
            else:
                messages.success(request, 'Welcome, {}'.format(user.get_full_name()))
                return redirect('dashboard')
        else:
            messages.info(request, 'Incorrect email or password')
    
    if request.method == 'POST':
        starter_form = StarterForm(request.POST)
        if starter_form.is_valid():
            user = starter_form.save(commit=False)
            user.save()
            
            try:
                group = Group.objects.get(id=1)
                group.user_set.add(user)
            except Group.DoesNotExist:
                messages.error(request, 'Group is not available, please contact support!')

            messages.success(request, 'Congratulation! You`re all set. Please login to continue.')
            return redirect('index')
    else:
        starter_form = AccountsCreationForm()
    
    context = {'next_url': next_url, 'starter_form': starter_form}
    return render(request, 'index/index.html', context)

@login_required
def dashboard(request):
    school_info = cache.get('dapodik_school')
    dapodik_employees_data = cache.get('dapodik_employees')
    if dapodik_employees_data is not None:
        count_emp = len(dapodik_employees_data)
    else:
        count_emp = 0
    dapodik_students_data = cache.get('dapodik_students')
    if dapodik_students_data is not None:
        count_std = len(dapodik_students_data)
    else:
        count_std = 0
    count_ltr = Students_Letter.objects.count() + Employees_Letter.objects.count() + Common_Letter.objects.count()
    count_sl_ts_m = Students_Letter.objects.filter(Q(type_sign='2') | (Q(type_sign='1') & ~Q(digital_sign_at__isnull=True))).count()
    count_el_ts_m = Employees_Letter.objects.filter(Q(type_sign='2') | (Q(type_sign='1') & ~Q(digital_sign_at__isnull=True))).count()
    count_cl_ts_m = Common_Letter.objects.filter(Q(type_sign='2') | (Q(type_sign='1') & ~Q(digital_sign_at__isnull=True))).count()

    count_arc = count_sl_ts_m + count_el_ts_m + count_cl_ts_m

    count_rs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=False).count
    count_rtd = Students_Letter.objects.filter(is_selected_to_destroy=True).count

    last_created_sl = Students_Letter.objects.order_by('-created_at')[:3]
    letter_done_sl = Students_Letter.objects.exclude(digital_sign_at__isnull=True).order_by('-digital_sign_at')[:3]
    lc_timesince_sl = Students_Letter.objects.order_by('-created_at')[:1]
    ld_timesince_sl = Students_Letter.objects.order_by('-digital_sign_at')[:1]

    last_created_el = Employees_Letter.objects.order_by('-created_at')[:3]
    letter_done_el = Employees_Letter.objects.exclude(digital_sign_at__isnull=True).order_by('-digital_sign_at')[:3]
    lc_timesince_el = Employees_Letter.objects.order_by('-created_at')[:1]
    ld_timesince_el = Employees_Letter.objects.order_by('-digital_sign_at')[:1]

    staging_scs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=True).order_by('-created_at')
    staging_ecs = Employees_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=True).order_by('-created_at')
    count_staging_scs = staging_scs.count()
    count_staging_ecs = staging_ecs.count()
    count_staging_hoa = count_staging_scs + count_staging_ecs

    context = {
        'school_info': school_info, 
        'count_emp': count_emp, 
        'count_std': count_std, 
        'count_ltr': count_ltr, 
        'count_arc': count_arc, 
        'count_rs': count_rs,
        'count_rtd': count_rtd,
        'last_created_sl': last_created_sl,
        'letter_done_sl': letter_done_sl,
        'lc_timesince_sl': lc_timesince_sl,
        'ld_timesince_sl': ld_timesince_sl,
        'last_created_el': last_created_el,
        'letter_done_el': letter_done_el,
        'lc_timesince_el': lc_timesince_el,
        'ld_timesince_el': ld_timesince_el,
        'count_staging_scs': count_staging_scs,
        'count_staging_ecs': count_staging_ecs,
        'count_staging_hoa': count_staging_hoa,
        }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def students(request):
    context = {'students': cache.get('dapodik_students'), 'config': config}
    return render(request, 'reference_data/students/students.html', context)

@login_required
def employees(request):
    context = {'employees': cache.get('dapodik_employees'), 'config': config}
    return render(request, 'reference_data/employees/employees.html', context)

@login_required
@group_required(config.opr)
def accounts(request):
    users =  User.objects.filter(is_superuser=False, is_staff=False)

    if request.method == 'POST':
        form = AccountsCreationForm(request.POST)
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
        form = AccountsCreationForm()

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
    digital_sign = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=False)
    students_digital_sign_applied = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=False).order_by('-digital_sign_at')[:9]
    count_rs = digital_sign.count

    context = {'digital_sign': digital_sign, 'students_digital_sign_applied':students_digital_sign_applied, 'count_rs': count_rs}
    return render(request, 'administration/sign_request/sign_request.html', context)

@login_required
@group_required(config.prl)
def check_letter(request, letter_id):
    letter = get_object_or_404(Students_Letter, letter_id=letter_id)
    return render(request, 'administration/sign_request/check_letter/check_letter.html', {'letter': letter})

@login_required
@group_required(config.prl)
def apply_signature(request, letter_id):
    start_time = time.time()
    letter = get_object_or_404(Students_Letter, letter_id=letter_id)
    letter.digital_sign_at = timezone.now()
    letter.digital_sign_by = request.user
    letter.digital_sign_by_name = request.user.get_full_name()
    letter.digital_sign_job_title = request.user.groups.first().name
    letter.digital_sign_institution = cache.get('dapodik_school')['nama']

    ip_address = requests.get('https://api.ipify.org/').text
    
    if not ip_address:
        ip_address = request.META.get('REMOTE_ADDR')

    letter.digital_sign_ip = ip_address

    handler = ipinfo.getHandler('f2ce563eb2923e') # Key owner 2019470089@student.umj.ac.id
    details = handler.getDetails(ip_address)

    if hasattr(details, 'city') and hasattr(details, 'country'):
        location = details.city + ', ' + details.country + ', ' + details.loc
        letter.digital_sign_location = location
    else:
        letter.digital_sign_location = 'Unknown'

    letter.digital_sign_number = hashlib.sha256(str(letter_id).encode()).hexdigest()
    digital_sign_url = reverse('archives-students-letter-check', kwargs={'letter_id': letter_id})
    letter.digital_sign_url = digital_sign_url

    qr_data = 'http://faturras-m1.local:8080'+digital_sign_url
    qr_code = qrcode.make(qr_data)
    buffer = BytesIO()
    qr_code.save(buffer)
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    letter.qr_code_base64 = qr_code_base64

    end_time = time.time()
    processing_time = end_time - start_time

    messages.success(request, 'Letter has been signed! {0:.2f}s'.format(processing_time))
    letter.save()

    return redirect('sign-request')


@login_required
@group_required(config.hoa, config.scs, config.ecs)
def request_queue(request):
    staging_scs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=True).order_by('-created_at')
    digital_sign_scs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=False).order_by('-created_at')
    students_digital_sign_applied_scs = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=False).order_by('-created_at')
    manual_sign_scs = Students_Letter.objects.filter(type_sign='2').order_by('-created_at')
    
    staging_ecs = Employees_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=True).order_by('-created_at')
    digital_sign_ecs = Employees_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True, is_in_staging=False).order_by('-created_at')
    students_digital_sign_applied_ecs = Employees_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=False).order_by('-created_at')
    manual_sign_ecs = Employees_Letter.objects.filter(type_sign='2').order_by('-created_at')

    context = {
        'staging_scs': staging_scs, 
        'digital_sign_scs': digital_sign_scs, 
        'students_digital_sign_applied_scs': students_digital_sign_applied_scs, 
        'manual_sign_scs': manual_sign_scs,
        
        'staging_ecs': staging_ecs, 
        'digital_sign_ecs': digital_sign_ecs, 
        'students_digital_sign_applied_ecs': students_digital_sign_applied_ecs, 
        'manual_sign_ecs': manual_sign_ecs
        }
    
    return render(request, 'administration/request_queue/request_queue.html', context)

@login_required
@group_required(config.scs, config.ecs)
def cancel_request_sign(request, letter_id):
    if request.user.groups.filter(name=config.scs).exists():
        letter = Students_Letter.objects.get(pk=letter_id)
    elif request.user.groups.filter(name=config.ecs).exists():
        letter = Employees_Letter.objects.get(pk=letter_id)
    elif request.user.groups.filter(name=config.hoa).exists():
        try:
            letter = Students_Letter.objects.get(pk=letter_id)
        except Students_Letter.DoesNotExist:
            try:
                letter = Employees_Letter.objects.get(pk=letter_id)
            except Employees_Letter.DoesNotExist:
                letter = None
    
    if letter:
        letter.is_in_staging = True
        letter.updated_by = request.user
        letter.save()
        messages.success(request, 'Request has been canceled!')
    else:
        messages.error(request, 'Request was failed to cancel!')
        
    return redirect('request-queue')

@login_required
@group_required(config.scs, config.ecs)
def send_sign_request(request, letter_id):
    if request.user.groups.filter(name=config.scs).exists():
        letter = Students_Letter.objects.get(pk=letter_id)
    elif request.user.groups.filter(name=config.ecs).exists():
        letter = Employees_Letter.objects.get(pk=letter_id)
    elif request.user.groups.filter(name=config.hoa).exists():
        try:
            letter = Students_Letter.objects.get(pk=letter_id)
        except Students_Letter.DoesNotExist:
            try:
                letter = Employees_Letter.objects.get(pk=letter_id)
            except Employees_Letter.DoesNotExist:
                letter = None

    if letter:
        letter.is_in_staging = False
        letter.updated_by = request.user
        letter.save()
        messages.success(request, 'Request was successfully sent!')
    else:
        messages.error(request, 'Request was failed to send!')

    return redirect('request-queue')


@login_required
@group_required(config.hoa, config.scs, config.ecs, config.prl, config.opr)
def generate_pdf(request, letter_id):
    letter = get_object_or_404(Students_Letter, letter_id=letter_id)
    digital_sign = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True)

    for qrc in digital_sign:
        qrc.generate_qr_code()

    template = get_template('administration/letter/letter_templates/students_letter/surat_keterangan.html')
    context = {'letter': letter}
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{letter.get_letter_type_display}_{letter_id}.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response


@login_required
def guest_book(request):
    guest_list = Guest_Book.objects.all().order_by('-created_at')

    context = {'guest_list': guest_list}
    return render(request, 'administration/guest_book/guest_book.html', context)

def guest_and_request_form(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted!')
            return redirect('guest-and-request-form')
    else:
        form = GuestBookForm()
    
    context = {'form': form}
    return render(request, 'administration/guest_book/guest_and_request_form/guest_and_request_form.html', context)

@login_required
def archives(request):
    students_digital_sign_applied = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=False).order_by('-created_at')

    context = {'students_digital_sign_applied': students_digital_sign_applied}
    return render(request, 'administration/archives/archives.html', context)

# @login_required
def archives_students_letter_check(request, letter_id):
    letter = get_object_or_404(Students_Letter, letter_id=letter_id)
    return render(request, 'administration/archives/archives_students_letter_check/archives_students_letter_check.html', {'letter': letter})

@login_required
@group_required(config.hoa)
def trash(request):
    students_digital_sign_applied = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=False, is_selected_to_destroy=False).order_by('-digital_sign_at')
    ready_to_destroy = Students_Letter.objects.filter(is_selected_to_destroy=True).order_by('-digital_sign_at')
    count_rtd = Students_Letter.objects.filter(is_selected_to_destroy=True).count

    context = {'students_digital_sign_applied': students_digital_sign_applied, 'ready_to_destroy': ready_to_destroy, 'count_rtd': count_rtd}
    return render(request, 'trash/trash.html', context)

@login_required
@group_required(config.hoa)
def process_sl_to_destroy_list(request, sl_arc_id):
    students_letter = Students_Letter.objects.get(pk=sl_arc_id)
    students_letter.is_selected_to_destroy = True
    students_letter.updated_by = request.user
    students_letter.save()

    messages.warning(request, 'Archive has been added to list!')
    return redirect('trash')

@login_required
@group_required(config.hoa)
def cancel_destroy_process_sl(request, archive_id):
    students_letter = Students_Letter.objects.get(pk=archive_id)
    students_letter.is_selected_to_destroy = False
    students_letter.updated_by = request.user
    students_letter.save()

    messages.info(request, 'Archive has been cancelled!')
    return redirect('trash')

@login_required
@group_required(config.hoa)
def process_destroy_sl(request, archive_id):
    students_letter = Students_Letter.objects.get(pk=archive_id)
    students_letter.delete()

    messages.error(request, 'Archive has been permanently destroyed!')
    return redirect('trash')
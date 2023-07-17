from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from integrations.data import dapodik_school, dapodik_employees, dapodik_students
from letter.models import Students_Letter
from .decorators import unauthenticated_user
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
    context = {'students': dapodik_students}
    return render(request, 'reference_data/students/students.html', context)

@login_required
def employees(request):
    context = {'employees': dapodik_employees}
    return render(request, 'reference_data/employees/employees.html', context)

def graduation(request):
    return render(request, 'reference_data/graduation/graduation.html')

@login_required
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
def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()

    messages.success(request, 'Account has been deleted!')
    return redirect('accounts')

@login_required
def deactivate_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()

    messages.success(request, 'Account has been deactivated!')
    return redirect('accounts')

@login_required
def activate_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()

    messages.success(request, 'Account has been activated!')
    return redirect('accounts')


@login_required
def sign_request(request):
    return render(request, 'administration/sign_request/sign_request.html')

@login_required
def request_queue(request):
    queue = Students_Letter.objects.all()
    digital_sign = Students_Letter.objects.filter(type_sign='1', digital_sign_at__isnull=True)
    manual_sign = Students_Letter.objects.filter(type_sign='2')

    context = {'queue': queue, 'digital_sign': digital_sign, 'manual_sign': manual_sign}
    return render(request, 'administration/request_queue/request_queue.html', context)

@login_required
def guest_book(request):
    return render(request, 'administration/guest_book/guest_book.html')

@login_required
def archives(request):
    return render(request, 'administration/archives/archives.html')

@login_required
def trash(request):
    return render(request, 'trash/trash.html')
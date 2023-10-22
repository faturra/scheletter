import time, requests
import socket
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.autoreload import restart_with_reloader
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.decorators import config, group_required
from .forms import IntegrationsForm
from .models import Integrations
from .data import update_api_data
from .system_check import dapodik_connection_status, check_telnet_connection

# Create your views here.
@login_required
@group_required(config.opr)
def setup_integration(request):
    def check_internet_connection():
        try:
            response = requests.get("http://www.google.com", timeout=5)
            if response.status_code == 200:
                return "1"
            else:
                return "0"
        except requests.RequestException:
            return "0"

    connection_status = check_internet_connection()

    def check_telnet_connection(host, port):
        try:
            with socket.create_connection((host, port), timeout=5) as sock:
                return '1'
        except (socket.timeout, ConnectionRefusedError):
            return '0'
        except socket.gaierror as e:
            print(f"Error: {e}")
            return '0'
        
    dapodik_connection_status = check_telnet_connection('api.smpn162jakarta.sch.id', 1162)

    integration_info = Integrations.objects.first()
    try:
        instance = Integrations.objects.get()
    except Integrations.DoesNotExist:
        instance = None

    if request.method == 'POST':
        start_time = time.time()
        form = IntegrationsForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.created_by = request.user
            instance.save()

            dapodik_school_api, dapodik_employees_api, dapodik_students_api = update_api_data()

            cache.set('dapodik_school', dapodik_school_api)
            cache.set('dapodik_employees', dapodik_employees_api)
            cache.set('dapodik_students', dapodik_students_api)

            if not (dapodik_school_api and dapodik_employees_api and dapodik_students_api):
                messages.warning(request, 'No data available, make sure the source information is correctly!')
            else:

                end_time = time.time()
                processing_time = end_time - start_time
                messages.success(request, 'Changes have been updated! {0:.2f}s'.format(processing_time))
            return redirect('setup-integration')
        else:
            form = IntegrationsForm()
            messages.error(request, 'Changes failed to update!')

    dapodik_school = cache.get('dapodik_school')
    dapodik_employees = cache.get('dapodik_employees')
    dapodik_students = cache.get('dapodik_students')

    if dapodik_school is None:
        dapodik_school = []

    if dapodik_employees is None:
        dapodik_employees = []

    if dapodik_students is None:
        dapodik_students = []

    count_school = len(dapodik_school)
    count_employees = len(dapodik_employees)
    count_students = len(dapodik_students)

    total_data = count_school + count_employees + count_students
    dapodik_status = dapodik_connection_status
    integration_connection_status = cache.get('dapodik_school')

    context = {
        'form': IntegrationsForm,
        'integration_info': integration_info,
        'integration_connection_status': integration_connection_status,
        'dapodik_status': dapodik_status,
        'total_data': total_data,
        'connection_status': connection_status
    }
    return render(request, 'integrations/setup_integration.html', context)


class ReloadServerView(View):
    def get(self, request):
        restart_with_reloader()
        return redirect('setup-integration')
    
@login_required
@group_required(config.opr)
def get_data_from_api_testing(request):
    data_text = str(cache.get('dapodik_school'))
    response = HttpResponse(data_text, content_type='text/plain')

    return response
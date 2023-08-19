import time
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.autoreload import restart_with_reloader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core import config, decorators
from .forms import IntegrationsForm
from .models import Integrations
from .data import dapodik_school
from .system_check import dapodik_connection_status

# Create your views here.

@login_required
@decorators.group_required(config.opr)
def setup_integration(request):
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
            end_time = time.time()
            processing_time = end_time - start_time

            messages.success(request, 'Changes have been updated! {0:.2f}s'.format(processing_time))
            return redirect('setup-integration')
        else:
            form = IntegrationsForm()
            messages.error(request, 'Changes failed to update!')

    dapodik_status = dapodik_connection_status
    integration_connection_status = dapodik_school

    context = {'form': IntegrationsForm, 'integration_info': integration_info, 'integration_connection_status': integration_connection_status, 'dapodik_status':dapodik_status}
    return render(request, 'integrations/setup_integration.html', context)


class ReloadServerView(View):
    def get(self, request):
        restart_with_reloader()
        return redirect('setup-integration')
    

def get_data_from_api_testing(request):
   
    data_text = str(dapodik_school)
    response = HttpResponse(data_text, content_type='text/plain')

    return response


def get_api_info(request):
    api_source = [
        {
            'server_address': 'http://api.smpn162jakarta.sch.id:1162/WebService/getSekolah?npsn=20100766',
            'token': 'ktuhMNbHJVY76ug',
        }
    ]
    return JsonResponse(api_source, safe=False)
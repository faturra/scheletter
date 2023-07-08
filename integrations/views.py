import time
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import IntegrationsForm
from .models import Integrations

# Create your views here.

@login_required
def setup_integration(request):
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

            messages.success(request, 'Changes have been saved! {0:.2f}s'.format(processing_time))
            return redirect('setup_integration')
        else:
            form = IntegrationsForm()
            messages.error(request, 'Changes failed to save!')

    context = {'form': IntegrationsForm}
    return render(request, 'integrations/setup_integration.html', context)
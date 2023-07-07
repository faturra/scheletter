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
        form = IntegrationsForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.created_by = request.user
            instance.save()

            messages.success(request, 'Changes have been saved!')
            return redirect('setup_integration')
        else:
            form = IntegrationsForm()
            messages.error(request, 'Changes failed to save!')

    context = {'form': IntegrationsForm}
    return render(request, 'integrations/setup_integration.html', context)
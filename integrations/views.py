from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import IntegrationsForm

# Create your views here.

@login_required(login_url='index')
def setup_integration(request):
    if request.method == 'POST':
        form = IntegrationsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()

            messages.success(request, 'Data successfully saved!')
            return redirect('setup_integration')
        else:
            form = IntegrationsForm()
            messages.error(request, 'Data failed to save!')

    context = {'form': IntegrationsForm}
    return render(request, 'integrations/setup_integration.html', context)
from django.shortcuts import render

# Create your views here.

def setup_integration(request):
    return render(request, 'integrations/setup_integration.html')
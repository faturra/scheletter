from django.shortcuts import render

# Create your views here.

def letter(request):
    return render(request, 'administration/letter/letter.html')
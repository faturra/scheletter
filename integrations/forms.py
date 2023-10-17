from django import forms
from .models import Integrations

class IntegrationsForm(forms.ModelForm):
    class Meta:
        model = Integrations
        fields = ['server_address', 'npsn', 'token']
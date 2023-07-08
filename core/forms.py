from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group
from django import forms
from django.forms.widgets import EmailInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions
from crispy_bootstrap5.bootstrap5 import FloatingField
from integrations.data import dapodik_employees

class CrispyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget = EmailInput()
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('username', placeholder='Email'),
            Field('password', placeholder='Password'),
            FormActions(
                Submit('submit', 'Login', css_class='btn-dark')
            )
        )

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.ChoiceField(choices=[], required=True, label='Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].choices = self.get_filtered_names()

    def get_filtered_names(self):
        role_a = 'Tenaga Administrasi Sekolah'
        role_b = 'Kepala Sekolah'
        filtered_names = [user['nama'] for user in dapodik_employees if user['jenis_ptk_id_str'] in [role_a, role_b]]
        sorted_names = sorted(filtered_names)
        return [(nama, nama) for nama in sorted_names]
    
    first_name = forms.ChoiceField(choices=[(user['nama'], user['nama']) for user in dapodik_employees], required=True, label='Name')
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Role')
    username = forms.CharField(widget=EmailInput(), label='Email')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name','group')
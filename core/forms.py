from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group, User
from django import forms
from django.forms.widgets import EmailInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions
# from integrations.data import cache.get('dapodik_employees')
from .models import Guest_Book
from django.core.cache import cache


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget = EmailInput()
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', placeholder='Email'),
            Field('password', placeholder='Password'),
            FormActions(
                Submit('submit', 'Login', css_class='btn-dark')
            )
        )

class AccountsCreationForm(UserCreationForm):
    first_name = forms.ChoiceField(choices=[], required=True, label='Name')
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Role')
    username = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
        label='Email'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].choices = self.get_filtered_names()

    def get_filtered_names(self):
        role_a = 'Tenaga Administrasi Sekolah'
        role_b = 'Kepala Sekolah'
        dapodik_employees = cache.get('dapodik_employees')

        if dapodik_employees is not None:
            filtered_names = [user['nama'] for user in dapodik_employees if user['jenis_ptk_id_str'] in [role_a, role_b]]
            sorted_names = sorted(filtered_names)
            return [(nama, nama) for nama in sorted_names]
        else:
            return []

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'group')


class StarterForm(UserCreationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
        label='Email'
    )

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')



class GuestBookForm(forms.ModelForm):
    class Meta:
        model = Guest_Book
        fields = ['name', 'address', 'occupation', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'required': True}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'required': True}),
            'occupation': forms.TextInput(attrs={'placeholder': 'Occupation', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'required': True}),
        }
        labels = {
            'name': 'Name',
            'address': 'Address',
            'occupation': 'Occupation',
            'email': 'Email',
            'message': 'Message',
        }
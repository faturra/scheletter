from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

class CrispyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = EmailInput()
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(
                Submit('submit', 'Login', css_class='btn-dark')
            )
        )

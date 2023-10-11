from django import forms
from django.core.cache import cache
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
# from integrations.data import cache.get('dapodik_students'), cache.get('dapodik_employees')
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from .models import Students_Letter, Employees_Letter, Common_Letter

# Student Letter Form
class StudentsLetterForm(forms.ModelForm):
    student_name = forms.ChoiceField(choices=[], required=True, label='Name')
    subject = forms.CharField(required=True, label='Regarding')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dapodik_students_name = [(item['nama'], item['nama']) for item in cache.get('dapodik_students')]
        choices_name = dapodik_students_name
        sorted_choices_name = sorted(choices_name, key=lambda x: x[1])
        self.fields['student_name'].choices = sorted_choices_name
       
    class Meta:
        model = Students_Letter
        fields = ['letter_type', 'student_name', 'student_class', 'student_gender', 'student_place_of_birth', 'student_date_of_birth', 'student_nisn', 'number', 'date', 'subject', 'body', 'type_sign']

        widgets = {
            'letter_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'student_name': forms.Select(attrs={'class': 'form-control', 'id': 'student-name-dropdown'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class', 'required': True, 'readonly': True}),
            'student_gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender', 'required': True, 'readonly': True}),
            'student_place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of birth', 'required': True, 'readonly': True}),
            'student_date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of birth', 'required': True, 'readonly': True}),
            'student_nisn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NISN', 'required': True, 'readonly': True}),
            'number': forms.HiddenInput(),
            'body': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'type_sign': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'date': DatePickerInput(options={'format': 'YYYY-MM-DD'}, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dapodik_students_name = [(item['nama'], item['nama']) for item in cache.get('dapodik_students')]
        choices_name = dapodik_students_name
        sorted_choices_name = sorted(choices_name, key=lambda x: x[1])
        self.fields['student_name'].choices = sorted_choices_name

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Field('letter_type', css_class='form-control', required=True),
                Field('student_name', css_class='form-control', id='student-name-dropdown', required=True),
                Field('student_class', css_class='form-control', placeholder='Class', readonly=True),
                Field('student_gender', css_class='form-control', placeholder='Gender', readonly=True),
                Field('student_place_of_birth', css_class='form-control', placeholder='Place of birth', readonly=True),
                Field('student_date_of_birth', css_class='form-control', placeholder='Date of birth', readonly=True),
                Field('student_nisn', css_class='form-control', placeholder='NISN', required=True),
                Field('number', css_class='form-control', placeholder='Auto', readonly=True),
                Field('date', css_class='form-control', placeholder='yyyy-mm-dd'),
                Field('subject', css_class='form-control', required=True),
                Field('body', css_class='form-control', required=True),
                Field('type_sign', css_class='form-control', required=True),
                css_class='col-md-12',
            )
        )

        self.helper.form_tag = False

# Employee Letter Form
class EmployeesLetterForm(forms.ModelForm):
    employee_name = forms.ChoiceField(choices=[], required=True, label='Name')
    subject = forms.CharField(required=True, label='Regarding')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dapodik_employees_name = [(item['nama'], item['nama']) for item in cache.get('dapodik_employees')]
        choices_name = dapodik_employees_name
        sorted_choices_name = sorted(choices_name, key=lambda x: x[1])
        self.fields['employee_name'].choices = sorted_choices_name
       
    class Meta:
        model = Employees_Letter
        fields = ['letter_type', 'employee_name', 'employee_rank', 'employee_gender', 'employee_place_of_birth', 'employee_date_of_birth', 'employee_empnumber', 'number', 'date', 'subject', 'body_opening', 'body_purpose', 'date_start', 'date_end', 'time_start', 'time_end', 'place_address', 'type_sign']

        widgets = {
            'letter_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'employee_rank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rank', 'required': True, 'readonly': True}),
            'employee_gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender', 'required': True, 'readonly': True}),
            'employee_place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Birth', 'required': True, 'readonly': True}),
            'employee_date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'required': True, 'readonly': True}),
            'employee_empnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EMP Number', 'required': True}),
            'number': forms.HiddenInput(),
            'body_opening': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'body_purpose': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'type_sign': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'date': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'date_start': DatePickerInput(
                options={'format': 'YYYY-MM-DD'},
                attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}
            ),
            'date_end': DatePickerInput(
                options={'format': 'YYYY-MM-DD'},
                attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}
            ),
            'time_start': TimePickerInput(
                options={'format': 'HH:mm', 'showClear': True},
                attrs={'class': 'form-control', 'placeholder': 'hh:mm'}
            ),
            'time_end': TimePickerInput(
                options={'format': 'HH:mm', 'showClear': True},
                attrs={'class': 'form-control', 'placeholder': 'hh:mm'}
            ),
        }

# Common Letter Form
class CommonLetterForm(forms.ModelForm):
    subject = forms.CharField(required=True, label='Regarding')
       
    class Meta:
        model = Common_Letter
        fields = ['letter_type', 'letter_category', 'dear_invitation', 'attachment', 'number', 'date', 'subject', 'body_opening', 'date_start', 'date_end', 'time_start', 'time_end', 'place_address', 'event_name', 'body_closing','type_sign']

        widgets = {
            'letter_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'letter_category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category', 'required': True}),
            'dear_invitation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dear/Invitation', 'required': True}),
            'number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Auto','readonly': True,}),
            'date': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'date_start': DatePickerInput(
                options={'format': 'YYYY-MM-DD'},
                attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}
            ),
            'date_end': DatePickerInput(
                options={'format': 'YYYY-MM-DD'},
                attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}
            ),
            'time_start': TimePickerInput(
                options={'format': 'HH:mm', 'showClear': True},
                attrs={'class': 'form-control', 'placeholder': 'hh:mm'}
            ),
            'time_end': TimePickerInput(
                options={'format': 'HH:mm', 'showClear': True},
                attrs={'class': 'form-control', 'placeholder': 'hh:mm'}
                ),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event', 'required': True}),
        }
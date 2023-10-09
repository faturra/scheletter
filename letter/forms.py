from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from integrations.data import dapodik_students_name, dapodik_learning_group, dapodik_employees_name
from .models import Students_Letter, Employees_Letter, Common_Letter

# Student Letter Form
class StudentsLetterForm(forms.ModelForm):
    student_name = forms.ChoiceField(choices=[], required=True, label='Name')
    subject = forms.CharField(required=True, label='Regarding')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices_name = dapodik_students_name
        sorted_choices_name = sorted(choices_name, key=lambda x: x[1])
        self.fields['student_name'].choices = sorted_choices_name
       
    class Meta:
        model = Students_Letter
        fields = ['letter_type', 'student_name', 'student_class', 'student_gender', 'student_place_of_birth', 'student_date_of_birth', 'student_nisn', 'number', 'date', 'subject', 'body', 'type_sign']

        widgets = {
            'letter_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'student_class': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Class','readonly': True,}),
            'student_gender': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Gender','readonly': True,}),
            'student_place_of_birth': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Place of birth','readonly': True,}),
            'student_date_of_birth': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd', 'required': True}),
            'student_nisn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NISN', 'required': True}),
            'number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Auto','readonly': True,}),
            'date': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
        }

# Employee Letter Form
class EmployeesLetterForm(forms.ModelForm):
    employee_name = forms.ChoiceField(choices=[], required=True, label='Name')
    subject = forms.CharField(required=True, label='Regarding')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices_name = dapodik_employees_name
        sorted_choices_name = sorted(choices_name, key=lambda x: x[1])
        self.fields['employee_name'].choices = sorted_choices_name
       
    class Meta:
        model = Employees_Letter
        fields = ['letter_type', 'employee_name', 'employee_rank', 'employee_gender', 'employee_place_of_birth', 'employee_date_of_birth', 'employee_empnumber', 'number', 'date', 'subject', 'body_opening', 'body_purpose', 'date_start', 'date_end', 'time_start', 'time_end', 'place_address', 'type_sign']

        widgets = {
            'letter_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'employee_place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Birth', 'required': True}),
            'employee_date_of_birth': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd', 'required': True}),
            'employee_empnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EMP Number', 'required': True}),
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
from django import forms
from crispy_forms.helper import FormHelper
from bootstrap_datepicker_plus.widgets import DatePickerInput
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Students_Letter

class StudentsLetterForm(forms.ModelForm):
    class Meta:
        model = Students_Letter
        fields = ['student_name', 'student_class', 'student_place_of_birth', 'student_date_of_birth', 'student_nisn', 'number', 'date', 'subject', 'body', 'type_sign']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class', 'required': True}),
            'student_place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Birth', 'required': True}),
            'student_date_of_birth': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd', 'required': True}),
            'student_nisn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NISN', 'required': True}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number',}),
            'date': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd',}),
        }
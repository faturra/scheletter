from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from integrations.data import dapodik_students_name, dapodik_learning_group
from .models import Students_Letter

class StudentsLetterForm(forms.ModelForm):
    student_name = forms.ChoiceField(choices=[], required=True, label='Name')
    student_class = forms.ChoiceField(choices=[], required=True, label='Class')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices_name = dapodik_students_name
        sorted_choices_name = sorted(choices_name, key=lambda x: x[1])
        self.fields['student_name'].choices = sorted_choices_name

        choices_class = dapodik_learning_group
        sorted_choices_class = sorted(choices_class, key=lambda x: x[1])
        self.fields['student_class'].choices = sorted_choices_class

    class Meta:
        model = Students_Letter
        fields = ['letter_type', 'student_name', 'student_class', 'student_place_of_birth', 'student_date_of_birth', 'student_nisn', 'number', 'date', 'subject', 'body', 'type_sign']

        widgets = {
            'student_place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Birth', 'required': True}),
            'student_date_of_birth': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd', 'required': True}),
            'student_nisn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NISN', 'required': True}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number'}),
            'date': DatePickerInput(options={
                'format': 'YYYY-MM-DD',
            }, attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
        }
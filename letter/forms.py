from django import forms
from .models import Students_Letter

class StudentsLetterForm(forms.ModelForm):
    class Meta:
        model = Students_Letter
        fields = ['number', 'date', 'subject', 'body', 'student_name', 'student_class', 'student_place_of_birth', 'student_date_of_birth', 'student_nisn', 'type_sign']
        
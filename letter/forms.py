from django import forms
from .models import Students_Letter

class StudentsLetterForm(forms.ModelForm):
    class Meta:
        model = Students_Letter
        fields = '__all__'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students_Letter(models.Model):
    type_sign_choice = (
        ('1', 'Digital Sign'),
        ('2', 'Manual Sign'),
    )

    letter_id = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, null=True)
    date = models.DateField()
    subject = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=300, null=True)
    student_name = models.CharField(max_length=100, null=True)
    student_class = models.CharField(max_length=100, null=True)
    student_place_of_birth = models.CharField(max_length=100, null=True)
    student_date_of_birth = models.DateField()
    student_nisn = models.CharField(max_length=100, null=True)
    type_sign = models.CharField(max_length=100, null=True, choices=type_sign_choice)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_models_letter', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_models_letter', null=True)
    digital_sign_at = models.DateTimeField(auto_now=True)
    digital_sign_by = models.CharField(max_length=100, null=True)
    digital_sign_job_title = models.CharField(max_length=100, null=True)
    digital_sign_institution = models.CharField(max_length=100, null=True)
    digital_sign_location = models.CharField(max_length=100, null=True)
    digital_sign_ip = models.CharField(max_length=100, null=True)
    digital_sign_number = models.CharField(max_length=100, null=True)
    digital_sign_url = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.number




# class Letter(models.Model):
#     letter_number = models.CharField(max_length=100, null=True)
#     letter_date = models.DateField()
#     letter_subject = models.CharField(max_length=100, null=True)
#     letter_body = models.TextField()
#     letter_signer = models.CharField(max_length=100, null=True)
#     letter_signer_position = models.CharField(max_length=100, null=True)
#     letter_signer_nip = models.CharField(max_length=100, null=True)
#     letter_signer_pangkat = models.CharField(max_length=100, null=True)
#     letter_signer_golongan = models.CharField(max_length=100, null=True)
#     letter_signer_unit = models.CharField(max_length=100, null=True)
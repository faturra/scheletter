from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students_Letter(models.Model):

    type_sign_choice = (
        ('1', 'Digital Sign'),
        ('2', 'Manual Sign'),
    )

    letter_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_class = models.CharField(max_length=50, null=True, blank=True)
    student_place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    student_date_of_birth = models.DateField()
    student_nisn = models.CharField(max_length=20, null=True, blank=True)
    type_sign = models.CharField(max_length=1, choices=type_sign_choice, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_students_letters', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_students_letters', null=True)
    digital_sign_at = models.DateTimeField(null=True, blank=True)
    digital_sign_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='digital_signed_students_letters', null=True)
    digital_sign_job_title = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_institution = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_location = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_ip = models.GenericIPAddressField(null=True, blank=True)
    digital_sign_number = models.CharField(max_length=50, null=True, blank=True)
    digital_sign_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.subject
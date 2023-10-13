import qrcode
import base64
from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image

# Create your models here.

# Students Letter Model
class Students_Letter(models.Model):

    letter_type_choice = (
        ('1', 'Surat Keterangan'),
    )

    type_sign_choice = (
        ('1', 'Digital Sign'),
        ('2', 'Manual Sign'),
    )


    letter_id = models.AutoField(primary_key=True)
    letter_type = models.CharField(max_length=1, choices=letter_type_choice, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=1000, null=True, blank=True)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_class = models.CharField(max_length=50, null=True, blank=True)
    student_gender = models.CharField(max_length=100, null=True, blank=True)
    student_place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    student_date_of_birth = models.DateField()
    student_nisn = models.CharField(max_length=20, null=True, blank=True)
    type_sign = models.CharField(max_length=1, choices=type_sign_choice, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_students_letters', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_students_letters', null=True)
    digital_sign_at = models.DateTimeField(null=True, blank=True)
    digital_sign_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='digital_signed_students_letters', null=True)
    digital_sign_by_name = models.CharField(max_length=150, null=True, blank=True)
    digital_sign_job_title = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_institution = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_location = models.CharField(max_length=1000, null=True, blank=True)
    digital_sign_ip = models.CharField(max_length=50, null=True, blank=True)
    digital_sign_number = models.CharField(max_length=512, null=True, blank=True)
    digital_sign_url = models.CharField(max_length=1000, null=True, blank=True)
    qr_code_base64 = models.TextField(null=True, blank=True)
    is_in_staging = models.BooleanField(default=True)
    is_selected_to_destroy = models.BooleanField(default=False)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.digital_sign_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        qr_byte_array = BytesIO()
        img.save(qr_byte_array, format='PNG')
        qr_bytes = qr_byte_array.getvalue()

        qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')

        self.qr_code_base64 = qr_base64

    def __str__(self):
        return self.number
    
# Employees Letter Model
class Employees_Letter(models.Model):

    letter_type_choice = (
        ('1', 'Surat Tugas'),
    )

    type_sign_choice = (
        ('1', 'Digital Sign'),
        ('2', 'Manual Sign'),
    )


    letter_id = models.AutoField(primary_key=True)
    letter_type = models.CharField(max_length=1, choices=letter_type_choice, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    body_opening = models.TextField(max_length=250, null=True, blank=True)
    body_purpose = models.TextField(max_length=325, null=True, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.CharField(max_length=50, null=True, blank=True)
    time_end = models.CharField(max_length=50, null=True, blank=True)
    place_address = models.CharField(max_length=600, null=True, blank=True)
    employee_name = models.CharField(max_length=100, null=True, blank=True)
    employee_place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    employee_date_of_birth = models.DateField()
    employee_rank = models.CharField(max_length=50, null=True, blank=True)
    employee_gender = models.CharField(max_length=100, null=True, blank=True)
    employee_empnumber = models.CharField(max_length=18, null=True, blank=True)
    type_sign = models.CharField(max_length=1, choices=type_sign_choice, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_employees_letters', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_employees_letters', null=True)
    digital_sign_at = models.DateTimeField(null=True, blank=True)
    digital_sign_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='digital_signed_employees_letters', null=True)
    digital_sign_by_name = models.CharField(max_length=150, null=True, blank=True)
    digital_sign_job_title = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_institution = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_location = models.CharField(max_length=1000, null=True, blank=True)
    digital_sign_ip = models.CharField(max_length=50, null=True, blank=True)
    digital_sign_number = models.CharField(max_length=512, null=True, blank=True)
    digital_sign_url = models.CharField(max_length=1000, null=True, blank=True)
    qr_code_base64 = models.TextField(null=True, blank=True)
    is_in_staging = models.BooleanField(default=True)
    is_selected_to_destroy = models.BooleanField(default=False)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.digital_sign_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        qr_byte_array = BytesIO()
        img.save(qr_byte_array, format='PNG')
        qr_bytes = qr_byte_array.getvalue()

        qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')

        self.qr_code_base64 = qr_base64

    def __str__(self):
        return self.number
    
# Common Letter Model
class Common_Letter(models.Model):

    letter_type_choice = (
        ('1', 'Surat Undangan'),
    )

    letter_category_choice = (
        ('1', 'Rahasia'),
        ('2', 'Segera'),
        ('3', 'Biasa'),
        ('4', 'Penting Segera'),
        ('5', 'Penting'),
    )

    type_sign_choice = (
        ('1', 'Digital Sign'),
        ('2', 'Manual Sign'),
    )


    letter_id = models.AutoField(primary_key=True)
    letter_type = models.CharField(max_length=1, choices=letter_type_choice, null=True, blank=True)
    letter_category = models.CharField(max_length=1, choices=letter_category_choice, null=True, blank=True)
    dear_invitation = models.CharField(max_length=100, null=True, blank=True)
    attachment = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    body_opening = models.TextField(max_length=250, null=True, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.CharField(max_length=50, null=True, blank=True)
    time_end = models.CharField(max_length=50, null=True, blank=True)
    place_address = models.CharField(max_length=600, null=True, blank=True)
    event_name = models.CharField(max_length=100, null=True, blank=True)
    body_closing = models.TextField(max_length=325, null=True, blank=True)
    type_sign = models.CharField(max_length=1, choices=type_sign_choice, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_common_letters', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_common_letters', null=True)
    digital_sign_at = models.DateTimeField(null=True, blank=True)
    digital_sign_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='digital_signed_common_letters', null=True)
    digital_sign_by_name = models.CharField(max_length=150, null=True, blank=True)
    digital_sign_job_title = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_institution = models.CharField(max_length=100, null=True, blank=True)
    digital_sign_location = models.CharField(max_length=1000, null=True, blank=True)
    digital_sign_ip = models.CharField(max_length=50, null=True, blank=True)
    digital_sign_number = models.CharField(max_length=512, null=True, blank=True)
    digital_sign_url = models.CharField(max_length=1000, null=True, blank=True)
    qr_code_base64 = models.TextField(null=True, blank=True)
    is_in_staging = models.BooleanField(default=True)
    is_selected_to_destroy = models.BooleanField(default=False)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.digital_sign_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        qr_byte_array = BytesIO()
        img.save(qr_byte_array, format='PNG')
        qr_bytes = qr_byte_array.getvalue()

        qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')

        self.qr_code_base64 = qr_base64

    def __str__(self):
        return self.number
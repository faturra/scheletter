from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
from .models import Students_Letter, Employees_Letter
import pytz

@receiver(pre_save, sender=Students_Letter)
@receiver(pre_save, sender=Employees_Letter)
def generate_surat_number(sender, instance, **kwargs):
    if not instance.number:
        latest_student_letter = Students_Letter.objects.order_by('-created_at').first()
        latest_employee_letter = Employees_Letter.objects.order_by('-created_at').first()

        latest_letter = max(
            (latest_student_letter, latest_employee_letter),
            key=lambda x: x.created_at.replace(tzinfo=None) if x and x.created_at else datetime.min
        )

        if latest_letter and latest_letter.number:
            latest_number = int(latest_letter.number.split(' ')[0])
            new_number = latest_number + 1
        else:
            new_number = 1

        year = instance.date.year

        if isinstance(instance, Employees_Letter) and not instance.number:
            instance.number = f'{new_number:03d} / PK.02.00'
        elif not instance.number:
            instance.number = f'{new_number:03d} TAHUN {year}'

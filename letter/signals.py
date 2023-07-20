from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Students_Letter

@receiver(pre_save, sender=Students_Letter)
def generate_surat_number(sender, instance, **kwargs):
    if not instance.number:
        latest_surat = Students_Letter.objects.order_by('-created_at').first()
        if latest_surat and latest_surat.number:
            latest_number = int(latest_surat.number.split(' ')[0])
            new_number = latest_number + 1
        else:
            new_number = 1
        year = instance.date.year
        instance.number = f'{new_number:03d} TAHUN {year}'

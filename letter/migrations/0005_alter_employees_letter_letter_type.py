# Generated by Django 3.2.6 on 2023-08-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0004_auto_20230808_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_letter',
            name='letter_type',
            field=models.CharField(blank=True, choices=[('1', 'Surat Tugas')], max_length=1, null=True),
        ),
    ]

# Generated by Django 3.2.6 on 2023-10-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0011_alter_students_letter_letter_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_letter',
            name='body_opening',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employees_letter',
            name='body_purpose',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employees_letter',
            name='place_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='employees_letter',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students_letter',
            name='body',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='students_letter',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 3.2.6 on 2024-02-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0013_auto_20240215_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='common_letter',
            name='destroyed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees_letter',
            name='destroyed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='students_letter',
            name='destroyed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

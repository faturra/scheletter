# Generated by Django 3.2.6 on 2023-07-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_students_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_letter',
            name='body',
            field=models.TextField(blank=True, max_length=1250, null=True),
        ),
    ]

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Initialize groups in the database'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Operator')
        if created:
            self.stdout.write(self.style.SUCCESS('Group "Operator" has been created.'))

        group, created = Group.objects.get_or_create(name='Student Correspondence Staff')
        if created:
            self.stdout.write(self.style.SUCCESS('Group "Student Correspondence Staff" has been created.'))

        group, created = Group.objects.get_or_create(name='Employee Correspondence Staff')
        if created:
            self.stdout.write(self.style.SUCCESS('Group "Employee Correspondence Staff" has been created.'))

        group, created = Group.objects.get_or_create(name='Head of Administration')
        if created:
            self.stdout.write(self.style.SUCCESS('Group "Head of Administration" has been created.'))

        group, created = Group.objects.get_or_create(name='Principal')
        if created:
            self.stdout.write(self.style.SUCCESS('Group "Principal" has been created.'))

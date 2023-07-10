from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from letter.views import *

urlpatterns = [
    path('', letter, name='letter'),
    path('create-blank-letter/student-letter', student_letter, name='student_letter'),
    path('create-blank-letter/employee-letter', employee_letter, name='employee_letter'),
    path('create-blank-letter/common-letter', common_letter, name='common_letter'),
]

from django.urls import path
from letter import views

urlpatterns = [
    path('', views.letter, name='letter'),
    path('create-blank-letter/student-letter', views.student_letter, name='student-letter'),
    path('create-blank-letter/employee-letter', views.employee_letter, name='employee-letter'),
    path('create-blank-letter/common-letter', views.common_letter, name='common-letter'),
]

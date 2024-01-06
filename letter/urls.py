from django.urls import path
from letter import views

urlpatterns = [
    path('', views.letter, name='letter'),
    path('create-blank-letter/student-letter', views.student_letter, name='student-letter'),
    path('edit-letter/student-letter/<int:letter_id>', views.edit_student_letter, name='edit-student-letter'),
    path('delete-letter/student-letter/<int:letter_id>', views.delete_student_letter, name='delete-student-letter'),
    path('create-blank-letter/employee-letter', views.employee_letter, name='employee-letter'),
    path('create-blank-letter/common-letter', views.common_letter, name='common-letter'),
    path('get-student-info', views.get_student_info, name='get-student-info'),
    path('get-employee-info', views.get_employee_info, name='get-employee-info'),
]

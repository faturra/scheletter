from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('welcome', views.dashboard, name='dashboard'),
    path('data-reference/students', views.students, name='students'),
    path('data-reference/employees', views.employees, name='employees'),
    path('accounts/employees', views.accounts, name='accounts'),
    path('accounts/user/delete/<int:user_id>/', views.delete_user, name='delete-user'),
    path('accounts/user/deactivate/<int:user_id>/', views.deactivate_user, name='deactivate-user'),
    path('accounts/user/activate/<int:user_id>/', views.activate_user, name='activate-user'),
    path('administration/request-queue', views.request_queue, name='request-queue'),
    path('administration/request-queue/cancel-request/<int:letter_id>/', views.cancel_request_sign, name='cancel-request-sign'),
    path('administration/request-queue/sending-request/<int:letter_id>/', views.send_sign_request, name='send-sign-request'),
    path('administration/sign-request', views.sign_request, name='sign-request'),
    path('administration/sign-request/check-letter/sl/<int:letter_id>/', views.check_letter_student, name='check-letter-student'),
    path('administration/sign-request/check-letter/el/<int:letter_id>/', views.check_letter_employee, name='check-letter-employee'),
    path('administration/sign-request/check-letter/cl/<int:letter_id>/', views.check_letter_common, name='check-letter-common'),
    path('administration/sign-request/check-letter/apply-signature/sl/<int:letter_id>/', views.apply_signature_sl, name='apply-signature-sl'),
    path('administration/sign-request/check-letter/apply-signature/el/<int:letter_id>/', views.apply_signature_el, name='apply-signature-el'),
    path('administration/sign-request/check-letter/apply-signature/cl/<int:letter_id>/', views.apply_signature_cl, name='apply-signature-cl'),
    path('administration/guest-and-request-form', views.guest_and_request_form, name='guest-and-request-form'),
    path('administration/guest-book', views.guest_book, name='guest-book'),
    path('administration/archives', views.archives, name='archives'),
    path('administration/archives/letters/verify/sl/<int:letter_id>', views.archives_students_letter_check, name='archives-students-letter-check'),
    path('administration/archives/letters/verify/el/<int:letter_id>', views.archives_employees_letter_check, name='archives-employees-letter-check'),
    path('administration/archives/letters/verify/cl/<int:letter_id>', views.archives_common_letter_check, name='archives-common-letter-check'),
    path('administration/archives/letters/view/sl/<int:letter_id>/', views.generate_pdf_sl, name='generate-pdf-sl'),
    path('administration/archives/letters/view/el/<int:letter_id>/', views.generate_pdf_el, name='generate-pdf-el'),
    path('administration/archives/letters/view/cl/<int:letter_id>/', views.generate_pdf_cl, name='generate-pdf-cl'),
    path('trash', views.trash, name='trash'),
    path('trash/selected/<int:sl_arc_id>/', views.process_sl_to_destroy_list, name='process-sl-to-destroy-list'),
    path('trash/cancel/<int:archive_id>/', views.cancel_destroy_process_sl, name='cancel-destroy-process-sl'),
    path('trash/process-to-destroy/<int:archive_id>/', views.process_destroy_sl, name='process-destroy-sl')
]
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('welcome', views.dashboard, name='dashboard'),
    path('data-reference/students', views.students, name='students'),
    path('data-reference/employees', views.employees, name='employees'),
    path('data-reference/graduation', views.graduation, name='graduation'),
    path('accounts/employees', views.accounts, name='accounts'),
    path('accounts/user/delete/<int:user_id>/', views.delete_user, name='delete-user'),
    path('accounts/user/deactivate/<int:user_id>/', views.deactivate_user, name='deactivate-user'),
    path('accounts/user/activate/<int:user_id>/', views.activate_user, name='activate-user'),
    path('administration/sign-request', views.sign_request, name='sign-request'),
    path('administration/request-queue', views.request_queue, name='request-queue'),
    path('administration/guest-book', views.guest_book, name='guest-book'),
    path('administration/archives', views.archives, name='archives'),
    path('trash', views.trash, name='trash'),
]
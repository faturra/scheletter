from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    # path('', auth_views.LoginView.as_view(template_name='index/index.html'), name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('welcome', dashboard, name='dashboard'),
    path('data-reference/students', students, name='students'),
    path('data-reference/employees', employees, name='employees'),
    path('data-reference/graduation', graduation, name='graduation'),
    path('accounts/employees', accounts, name='accounts'),
    path('accounts/user/delete/<int:user_id>/', delete_user, name='delete-user'),
    path('accounts/user/deactivate/<int:user_id>/', deactivate_user, name='deactivate-user'),
    path('accounts/user/activate/<int:user_id>/', activate_user, name='activate-user'),
    path('administration/sign-request', sign_request, name='sign-request'),
    path('administration/request-queue', request_queue, name='request-queue'),
    path('administration/guest-book', guest_book, name='guest-book'),
    path('administration/archives', archives, name='archives'),
    path('trash', trash, name='trash'),
]

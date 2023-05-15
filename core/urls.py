from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('welcome', dashboard, name='dashboard'),
    path('data/core/students', students, name='students'),
    path('data/core/employees', employees, name='employees'),
    path('data/core/graduation', graduation, name='graduation'),
    path('accounts/employees', accounts, name='accounts'),
    path('administration/sign-request', sign_request, name='sign-request'),
    path('administration/request-queue', request_queue, name='request-queue'),
    path('administration/guest-book', guest_book, name='guest-book'),
    path('administration/archives', archives, name='archives'),
    path('trash', trash, name='trash'),
]

from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('welcome', dashboard, name='dashboard'),
]

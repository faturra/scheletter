from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('welcome', dashboard, name='dashboard'),
    path('data/core/students', students, name='students'),
    path('data/core/gtk', gtk, name='gtk'),
    path('data/core/graduation', graduation, name='graduation'),
]

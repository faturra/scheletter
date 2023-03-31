from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from letter.views import *

urlpatterns = [
    path('', letter, name='letter'),
]

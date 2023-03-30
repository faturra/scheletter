from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
from integrations.views import *

urlpatterns = [
    path('', setup_integration, name='setup_integration'),
]

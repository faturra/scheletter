from django.urls import path
from integrations import views

urlpatterns = [
    path('', views.setup_integration, name='setup-integration'),
]

from django.urls import path
from integrations import views

urlpatterns = [
    path('', views.setup_integration, name='setup-integration'),
    path('reload-server/', views.ReloadServerView.as_view(), name='reload-server'),
    path('get-data-api-now/', views.get_data_from_api_testing, name='get-data-api-now'),
]

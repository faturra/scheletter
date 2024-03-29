from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Integrations(models.Model):
    integration_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    server_address = models.CharField(max_length=200, null=True)
    npsn = models.CharField(max_length=200, null=True)
    token = models.CharField(max_length=200, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_models', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.npsn
from django.db import models

# Create your models here.
class Guest_Book(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
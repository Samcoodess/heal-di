from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class Documents(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='')
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_by')
    patient_name = models.CharField(max_length=255)  # Adjust this field based on your requirements

    def __str__(self):
        return self.title
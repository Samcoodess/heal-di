# models.py

from django.db import models
from django.conf import settings

class Calendar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()

class Symptoms(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    symptom_name = models.CharField(max_length=255)
    # Add other fields as needed

class MedRecords(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    record_name = models.CharField(max_length=255)
    # Add other fields as needed

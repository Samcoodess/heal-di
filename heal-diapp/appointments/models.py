# in medcalendar/models.py
from django.db import models

class Appointment(models.Model):
    patient = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you're using Django's User model
    healthcare_provider = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.patient.username} - {self.healthcare_provider} - {self.date_time}"

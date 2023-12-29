# appointments/models.py

from django.db import models
from accounts.models import User

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments', default=None)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments', default=None)
    location = models.CharField(max_length=255, default=None)
    name = models.CharField(max_length=255, default=None)
    address = models.TextField(default='opt out')

    def __str__(self):
        return f"{self.doctor.email} - {self.patient.email}"


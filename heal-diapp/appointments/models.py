from django.db import models
from django.contrib.auth import get_user_model

class Appointment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='appointments_as_user')
    healthcare_provider = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.user.username} - {self.healthcare_provider} - {self.date_time}"
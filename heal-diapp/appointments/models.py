from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Appointment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='appointments_as_user')
    name = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(default=0)  # Set a suitable default value
    location = models.CharField(max_length=255)
    note = models.TextField(default= 'I will call')
    date_time = models.DateTimeField(default=timezone.now)  # Set a default value
    confirmation_message = models.TextField(default='Your appointment is confirmed')  # Set a suitable default value

    def save(self, *args, **kwargs):
        # Set the default value for the 'name' field to the user's first name
        if not self.name and self.user:
            self.name = self.user.first_name

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} - {self.name} - {self.date_time}"

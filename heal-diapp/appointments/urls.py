

# appointments/urls.py
from django.urls import path
from .views import schedule_appointment

urlpatterns = [
    path('schedule/', schedule_appointment, name='schedule_appointment'),
    # Add other URL patterns as needed
]

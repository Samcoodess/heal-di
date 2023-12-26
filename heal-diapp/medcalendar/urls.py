

# appointments/urls.py
from django.urls import path
from .views import medcalendar

urlpatterns = [
    path('medcalendar/', medcalendar, name='medcalendar'),
    # Add other URL patterns as needed
]

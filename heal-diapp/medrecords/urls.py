

# appointments/urls.py
from django.urls import path
from .views import medrecords

urlpatterns = [
    path('medrecords/', medrecords, name='medrecords'),
    # Add other URL patterns as needed
]

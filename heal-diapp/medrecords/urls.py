

# appointments/urls.py
from django.urls import path
from .views import medrecords,upload_document

urlpatterns = [
    path('medrecords/', medrecords, name='medrecords'),
    # Add other URL patterns as needed
    path('medrecords/upload/', upload_document, name='upload_document'),
]

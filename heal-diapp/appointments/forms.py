# appointments/forms.py

from django import forms
from .models import Appointment

class Step1Form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['location']

class Step2Form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'address']

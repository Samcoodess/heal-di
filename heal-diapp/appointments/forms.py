# appointments/forms.py
from django import forms
from .models import Appointment

class Step1Form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'age', 'location', 'note']

class Step2Form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_time']
        widgets = {
            'date_time': forms.DateInput(attrs={'type': 'datetime-local'}),
            # Add any additional widgets for other fields
        }
class Step3Form(forms.Form):
    confirmation_message = forms.CharField(
        label='Confirmation Message',
        widget=forms.Textarea(attrs={'rows': 4})
    )

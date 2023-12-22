# appointments/views.py
from django.shortcuts import render

def schedule_appointment(request):
    return render(request, 'appointments/schedule_appointment.html')

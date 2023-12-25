# appointments/views.py
from django.shortcuts import render

def schedule_appointment(request):
    return render(request, 'f_app/schedule_appointment.html')

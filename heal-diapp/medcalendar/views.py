# appointments/views.py
from django.shortcuts import render

def medcalendar(request):
    return render(request, 'medcalendar.html')

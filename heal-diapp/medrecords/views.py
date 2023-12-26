# appointments/views.py
from django.shortcuts import render

def medrecords(request):
    return render(request, 'medrecords.html')

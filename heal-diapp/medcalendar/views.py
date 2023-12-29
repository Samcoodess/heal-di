# appointments/views.py
from django.shortcuts import render

def medcalendar(request):
    return render(request, 'medcalendar.html')


# views.py

from django.shortcuts import render
from .models import Calendar, Symptoms, MedRecords

def calendar_view(request):
    # Fetch calendar data and pass it to the template
    calendars = Calendar.objects.filter(user=request.user)
    return render(request, 'medcalendar/calendar_view.html', {'calendars': calendars})

from django.views import View

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        # Your view logic here
        return render(request, 'medcalendar/calendar.html', context={})
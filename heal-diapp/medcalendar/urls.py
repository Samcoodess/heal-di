# # medcalendar/urls.py
# from django.urls import path, include
# from .views import medcalendar, calendar_view
# from .views import CalendarView


# app_name = 'medcalendar'  # Set the app_name here

# urlpatterns = [
#     path('calendar/', include('schedule.urls')),


# ]


# medcalendar/urls.py
from django.urls import path
from .views import CalendarView

app_name = 'medcalendar'

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    # other URL patterns for the medcalendar app
]

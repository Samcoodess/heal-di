"""
doctor_appointment_system URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointment.views import PatientListView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('appointments.urls')),
    path('', include('appointment.urls')),
    path('', include('medrecords.urls')),
    # path('', include('medcalendar.urls')),
    path('schedule/', include(('schedule.urls', 'schedule'), namespace='schedule')),
    path('medcalendar/', include(('medcalendar.urls', 'medcalendar'), namespace='medcalendar')),




    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
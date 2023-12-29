# # appointments/urls.py
# from django.urls import path
# from .views import schedule_appointment, success_page

# urlpatterns = [
#     path('schedule/', schedule_appointment, name='schedule_appointment'),
#     path('success/', success_page, name='success_page'),  # Replace 'success_page' with your actual success page view
#     # Add more URLs as needed
# ]


from django.urls import path
# from .views import schedule_appointment, AppointmentWizardView, success_page
# from .forms import Step1Form, Step2Form, Step3Form
from .views import schedule_appointment_step1, schedule_appointment_step2


urlpatterns = [

    # path('schedule/', schedule_appointment, name='schedule_appointment'),
    # path('schedule/step2/', AppointmentWizardView.as_view([Step1Form, Step2Form]), name='schedule_appointment_step2'),
    # path('schedule/step3/', AppointmentWizardView.as_view([Step2Form, Step3Form]), name='schedule_appointment_step3'),
    # path('success/', success_page, name='success_page'),
    path('schedule/step1/', schedule_appointment_step1, name='schedule_step1'),
    path('schedule/step2/', schedule_appointment_step2, name='schedule_step2'),


]

# appointments/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Step1Form, Step2Form, Step3Form
from .models import Appointment
from formtools.wizard.views import SessionWizardView
from django.utils import timezone
from django.urls import reverse
from .models import Appointment




@login_required
def schedule_appointment(request):
    form = None  # Initialize the form variable with a default value

    if request.method == 'POST':
        print("POST request received")
        form = Step1Form(request.POST)
        if form.is_valid():
            print("Form is valid")
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            print("Appointment saved")
            return redirect('schedule_appointment_step2')
        else:
            print("Form is not valid")

    elif 'step2' in request.POST:
        form = Step2Form(request.POST)
        if form.is_valid():
            # Save data or handle as needed
            # Redirect to the next step or render the next form
            return redirect('schedule_appointment_step3')

    elif 'step3' in request.POST:
        form = Step3Form(request.POST)
        if form.is_valid():
            # Save data or handle as needed
            # Redirect to the confirmation page or render the confirmation form
            return redirect('success_page')

    else:
        pass
        # Invalid form submission or unknown step
        # Handle as needed

    # If the request is a GET or the form is not valid, the form variable remains None
    return render(request, 'appointments/schedule_appointment.html', {'form': form})


class AppointmentWizardView(SessionWizardView):
    template_name = 'appointments/appointment_wizard.html'
    form_list = [Step1Form, Step2Form, Step3Form]

    def done(self, form_list, **kwargs):
        # Handle the final form submission and save data as needed
        print("Done method executed")

        appointment_data = {
            'user': self.request.user,
            'name': form_list[0].cleaned_data['name'],
            'age': form_list[0].cleaned_data['age'],
            'location': form_list[0].cleaned_data['location'],
            'note': form_list[0].cleaned_data['note'],
            'date_time': form_list[1].cleaned_data.get('date_time', timezone.now()),  # Use get to handle None
            'confirmation_message': form_list[2].cleaned_data['confirmation_message']
        }

        appointment = Appointment.objects.create(**appointment_data)

        # Redirect to the success_page view
        return redirect(reverse('success_page'))

# views.py

@login_required
def success_page(request):
    # Get upcoming appointments for the logged-in user
    appointments = Appointment.objects.filter(user=request.user, date_time__gte=timezone.now())
    return render(request, 'appointments/success_page.html', {'appointments': appointments})

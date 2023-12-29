# appointments/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Step1Form, Step2Form

# appointments/views.py



@login_required
def schedule_appointment_step1(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            # Save form data to session
            request.session['location'] = form.cleaned_data['location']
            return redirect('schedule_step2')
    else:
        form = Step1Form()

    return render(request, 'appointments/schedule_step1.html', {'form': form})

def schedule_appointment_step2(request):
    if request.method == 'POST':
        form = Step2Form(request.POST)
        if form.is_valid():
            # Save form data to session
            request.session['name'] = form.cleaned_data['name']
            request.session['address'] = form.cleaned_data['address']
            return redirect('confirm_appointment')
    else:
        form = Step2Form()

    return render(request, 'appointments/schedule_step2.html', {'form': form})

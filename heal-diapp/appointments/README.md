# Appointments Module

## Overview

The `appointments` module is responsible for managing appointments within the Healdi application. This module facilitates the scheduling, viewing, and management of patient appointments with healthcare providers.

## Features

- **Appointment Scheduling:**
  - Users can schedule appointments with available healthcare providers.
  - The scheduling process is divided into multiple steps for ease of use.

- **Appointment Management:**
  - Healthcare providers can view and manage their scheduled appointments.
  - Patients can view upcoming and past appointments.

- **Calendar Integration:**
  - A calendar view provides an intuitive way to visualize scheduled appointments.

- **Patient Information:**
  - Capture essential patient information during the appointment scheduling process.




## Appointment Scheduling Process

### Step 1: Basic Information Form ✅

Patients provide basic information for the appointment:

- Name
- Age
- Location
- Additional Notes

### Step 2: Calendar View {under construction} 🚧

Users select a suitable date and time for the appointment using a calendar view.

### Step 3: Confirmation and Management 🚧

Healthcare providers can confirm or reschedule appointments. Patients can view confirmed appointments and receive notifications.

## Directory Structure

The `appointments` module follows a standard Django app directory structure:

## How to Use and debug

### 1. Installation

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
``````


### 2. Configuration
Ensure that the appointments app is included in the `INSTALLED_APPS` setting in healdi_main settings.py:

```
INSTALLED_APPS = [
     ...
    'appointments',
     ...
]
```
### 3. URL Configuration
Cleck the appointments URLs in healdi_main `urls.py`:


```
from django.urls import path, include

urlpatterns = [
    # ...
    path('appointments/', include('appointments.urls')),
    # ...
]
```

### 4. Run the Development Server
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/appointments/ in your web browser to access the appointments module.




## Contribution
Contributions are welcome and appreciated!❤️



## License
This project is licensed under the MIT License.

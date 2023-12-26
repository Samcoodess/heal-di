
# Heal-di 🩺🏥
Your health companion

## App

- django app is located [here](./heal-diapp/)
## Directory Structure

The `heal-diapp` project includes multiple Django apps:
- `appointments`
- `medrecords`
- `medcalendar`
- `accounts`

Each app follows a standard Django app directory structure.

## Features 

### Schedule Appointment App 🚧

- Appointment Scheduling
- Appointment Management
- Calendar Integration

### Medrecords App 🚧

- Electronic Medical Records
- Encrypted Record Management
- Document Upload

### Medcalendar App 🚧

- Health Calendar
- Reminders and Notifications

### Accounts App ⌛
- User Groups (Doctors, Patients)
- User Registration and Authentication
- Profile Management
- Password Recovery
- Login (Username & Password, Email & Password, Email or Username & Password, Remember Me)
- Logout


## Installing

### Clone the project

```
git clone git@github.com:Samcoodess/heal-di.git
cd heal-diapp
```

### Install dependencies & activate virtualenv

```
cd heal-diapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Administration

administrative interface is available on http://127.0.0.1:8000/admin/

- Create a superuser

```
python manage.py createsuperuser --email sam@superapp.com --username sam
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `heal-diapp/app/conf/development/settings.py` if you want to develop the project. Some of the interesting settings are the usage of sqlite3 database (can be opened with [sqlitebrowser](https://sqlitebrowser.org/) ) 

2. Edit `heal-diapp/app/conf/production/settings.py` if you want to run the project in production. This requires `IS_PRODUCTION`` env variable to activate state.


## Apply migrations

more about migrations - [here](https://docs.djangoproject.com/en/4.2/topics/migrations/)

```
python manage.py migrate
```

### Collect static files (only on a production server)

more info [here](https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/)

```
python manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```
python manage.py runserver
```

### Docker

#### Build docker image

```
cd ./heal-diapp/
docker build -t heal-app:latest .
```
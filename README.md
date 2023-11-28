# heal-di
A health companion

## App

- django app is located [here](./app/)
- 

## Features

- Login
    - via username & password
    - via email & password
    - via email or username & password
    - with a remember me checkbox (optional)
- Register
- Logout
- Profile activation via email
- Reset password
- Resend an activation code
- Change password
- Change profile
- Multilingual

## Installing

### Clone the project

```
git clone git@github.com:Samcoodess/heal-di.git
cd heal-di
```

### Install dependencies & activate virtualenv

```
cd app
python3 -m venv venv
source venv/bin/activate
```


## Administration

administrative interface is available on http://127.0.0.1:8000/admin/

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `app/app/conf/development/settings.py` if you want to develop the project.

2. Edit `app/app/conf/production/settings.py` if you want to run the project in production.


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

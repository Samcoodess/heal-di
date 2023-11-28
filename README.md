# heal-di
A health companion

## App

- django app is located [here](./heal-app/)

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
cd heal-app
```

### Install dependencies & activate virtualenv

```
cd heal-app
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

1. Edit `heal-app/app/conf/development/settings.py` if you want to develop the project. Some of the interesting settings are the usage of sqlite3 database (can be opened with [sqlitebrowser](https://sqlitebrowser.org/) ) 

2. Edit `heal-app/app/conf/production/settings.py` if you want to run the project in production. This requires `IS_PRODUCTION`` env variable to activate state.


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

# base image  
FROM python:3.9.18-alpine3.18
# setup environment variable  
ENV APP_HOME /app  
ENV APP_USER django-user
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# creating app user
RUN adduser --disabled-password --no-create-home $APP_USER

# set work directory  
RUN mkdir -p $APP_HOME  

# copy whole project to your docker home directory. 
COPY . $APP_HOME

# where your code lives  
WORKDIR $APP_HOME  

# permissions
RUN chown $APP_USER $APP_HOME
RUN chgrp $APP_USER $APP_HOME

# prep environment
RUN apk add --no-cache \
        mariadb-client \
        py3-mysqlclient \
        mysql-client \
        libffi \
        gettext \
        gettext-libs \
        jpeg-dev \
        zlib-dev \
        postgresql-dev \
        postgresql-client \
    && apk add --no-cache --virtual build-requirements \
        cargo \
        freetype-dev \
        gcc \
        libffi-dev \
        linux-headers \
        mariadb-dev \
        musl-dev \
        rust \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir virtualenv \
    && virtualenv /env \
    && /env/bin/pip install --no-cache-dir --upgrade \
        pip \
        uwsgi \
    && /env/bin/pip install -r requirements.txt \
    && apk del build-requirements \
    && rm -rf /root/.cache \
    && rm -rf /tmp

# switch user
USER $APP_USER

# port where the Django app runs  
EXPOSE 8000  

# add venv binaries
ENV PATH="/env/bin:$PATH"

# migration and static files
# TODO: move in docker-compose
RUN python manage.py collectstatic --noinput \
    && python manage.py migrate --noinput

# start server
# runs the production server
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "healdi_main.wsgi:application"]

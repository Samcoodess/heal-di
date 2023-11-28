FROM python:3.10

WORKDIR /heal-app

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

USER python

COPY --chown=python:python . .

ENV PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

RUN pip install --upgrade pip && pip install -r ./requirements.txt

RUN python manage.py collectstatic --no-input

ENTRYPOINT ["/heal-app/bin/docker-entrypoint-web"]

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "config.wsgi"]
FROM python:slim-bullseye

ARG BUILD_DEPS="build-essential git curl vim zip"
RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends $BUILD_DEPS

ENV DJANGO_SETTINGS_MODULE=yourapp.settings

WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /code/

EXPOSE 5111
CMD python manage.py runserver 0.0.0.0:5111

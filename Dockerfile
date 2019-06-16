#
# The doc: https://docs.docker.com/engine/reference/builder/#usage
# Dockerfile-drf-microservice
# Help from: https://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/
#

FROM python:3.6

# update system and install uwsgi
RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

# create target dir and copy requirement in
RUN mkdir -p /opt/drf-microservice
COPY requirements.txt /opt/drf-microservice/

# install all dependencies of the app
RUN pip3 install -r /opt/drf-microservice/requirements.txt

# copy the app cd change WORKDIR to app root
COPY . /opt/drf-microservice
WORKDIR /opt/drf-microservice

ENV DJANGO_ENV=stage
ENV DOCKER_CONTAINER=1
ENV SECRET_KEY=local
ENV ENABLE_DEBUG=1

EXPOSE 8000

CMD ["uwsgi", "--ini", "/opt/drf-microservice/uwsgi.ini"]
#CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "project:project"]
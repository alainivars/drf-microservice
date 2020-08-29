#
# The doc: https://docs.docker.com/engine/reference/builder/#usage
# Dockerfile-drf-microservice
# Help from: https://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/
#

FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /drf-microservice

# Set the working directory to /drf-microservice
WORKDIR /drf-microservice

# Copy the current directory contents into the container at /drf-microservice
ADD . /drf-microservice/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

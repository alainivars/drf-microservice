
.. include:: links.inc

Build and run the image with Docker
===================================

Build and run with docker-compose::

    docker-compose up

Then login, see API documentation

Build the Docker image::

    docker build -t drf-ms-sqlite:latest --label drf-ms-sqlite -f Dockerfile.sqlite .

Run the container::

    docker-compose up

Run the container as service::

    docker-compose up -d

Delete the container::

    docker-compose rm -f


.. warning:: WORK IN PROGRESS, not existing actually

Build the Docker image::

    docker build -t drf-ms-sqlite:latest --label drf-ms-sqlite -f Dockerfile.sqlite .
    #docker build -t my-nginx -f Dockerfile.nginx .

Initialise the application::

    docker run -v "$PWD/drf-microservice:/opt/drf-microservice" drf-ms_sqlite:latest django-admin startproject my_api .
    docker run --noreload --rm -v "$PWD/drf-microservice:/opt/drf-microservice" -e DJANGO_MANAGEMENT_JOB=makemigrations drf-ms_sqlite

Run the container::

    docker network create my-network
    docker run -d --name drf --net my-network -v /app my-drf
    docker run -d --name nginx --net my-network -p "5000:80" my-nginx

If you want to change the port binding, it's here...


.. include:: links.inc

Build and run the image with Docker 3 different way
===================================================
Note: All of them are for development and test env ONLY

Build and run the image, all with docker-compose
------------------------------------------------
You will need docker-compose compatible 3.8+ format, version 1.25.5+
https://github.com/docker/compose/releases/

Build and run with docker-compose::

    docker-compose -f docker-compose.drf-ms-sqlite.yml up


Delete the container, the network and the image::

    docker-compose -f docker-compose.drf-ms-sqlite.yml rm -f
    docker network rm drf-microservice_default
    docker rmi drf-ms-sqlite

1 Build the image with Docker and run with docker-compose
---------------------------------------------------------

Build the Docker image::

    docker build -t drf-ms-sqlite:latest --label drf-ms-sqlite -f Dockerfile .

Run the container::

    export DJANGO_SETTINGS_MODULE=my_api.settings.local
    docker-compose -f docker-compose.sqlite.yml up

2 Build and run the image with Docker
--------------------------------------

Build the Docker image::

    docker build -t drf-ms-sqlite:latest --label drf-ms-sqlite -f Dockerfile.sqlite .

Run the container as service::

    docker run -d -v "/home/a/repositories/dj/drf-microservice:/drf-microservice" -p 8000:8000 --name drf-ms-sqlite2 drf-ms-sqlite:latest


.. warning:: WORK IN PROGRESS AFTER THIS, not existing actually

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

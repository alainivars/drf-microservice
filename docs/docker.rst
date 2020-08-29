
.. include:: links.inc

Build and run the image with Docker 3 different way
===================================================
Note: All of them are for development and test env ONLY

Build and run the image, all with docker-compose
------------------------------------------------
Here docker-compose do every thing but you can't choice:
    - the container name
    - the image name

Build and run with docker-compose::

    docker-compose up

Delete the container::

    docker-compose rm -f


1 Build the image with Docker and run with docker-compose
---------------------------------------------------------

Build the Docker image::

    docker build -t drf-ms-sqlite:latest --label drf-ms-sqlite -f Dockerfile.sqlite .

Run the container::

    docker-compose up -f docker-compose.1.yml

2 Build and run the image with Docker
--------------------------------------

Build the Docker image::

    docker build -t drf-ms-sqlite:latest --label drf-ms-sqlite -f Dockerfile.sqlite .

Run the container as service::

    docker run -d -v "/home/a/repositories/dj/drf-microservice:/drf-microservice" -p 8000:8000 --name drf-ms-sqlite2 drf-ms-sqlite:latest


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

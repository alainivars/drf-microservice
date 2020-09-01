
.. include:: links.inc

Build and run the image with Docker 2 different way
===================================================
In both case, after the run, open a console to the docker container to run::

    docker images | grep drf-ms-sqlite
    Get the container id and with it:
    docker exec -it be64cad1af93 bash
    And inside the remote console:
    export DJANGO_SECRET_KEY=local; export DJANGO_SETTINGS_MODULE=my_api.settings.local; python manage.py createsuperuser

Build and run the image, all with docker-compose
------------------------------------------------
You will need docker-compose compatible 3.8+ format, version 1.25.5+
https://github.com/docker/compose/releases/

Build and run with docker-compose::

    docker-compose -f docker-compose.drf-ms-sqlite.yml up

Delete the container, the network and the image::

    docker-compose -f docker-compose.drf-ms-sqlite.yml rm -f
    docker network rm drf-microservice_default
    docker rmi drf-ms-sqlite:latest

Build and run the image with Docker
-----------------------------------

Build the Docker image::

    docker build -t drf-ms-sqlite:0.8.1wodc --label drf-ms-sqlite.wodc -f Dockerfile.drf-ms-sqlite.wodc .

Run the container as service::

    docker run -d -v "/home/a/repositories/dj/drf-microservice:/drf-microservice" -p 8000:8000 --name drf-ms-sqlite.wodc drf-ms-sqlite:0.8.1wodc

Stop, Delete the container and the image::

    docker stop drf-ms-sqlite.wodc
    docker rm drf-ms-sqlite.wodc
    docker rmi drf-ms-sqlite:0.8.1wodc


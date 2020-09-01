
.. include:: links.inc

Build and run the image with Docker
===================================

Pre-condition, set the required credential and secret::

    # postgres
    export POSTGRES_HOST=trust
    export POSTGRES_HOST_AUTH_METHOD=trust
    export POSTGRES_DB=postgres
    export POSTGRES_USER=postgres
    export POSTGRES_PASSWORD=postgres
    # django postgres dev and test
    export DB_ENGINE=django.db.backends.postgresql
    export DB_HOST=127.0.0.1
    export DB_PORT=5432
    export DB_NAME=drfms_db
    export DB_USER=drfms_user
    export DB_PASS=drfms_pass
    # django dev and test
    export DJANGO_ENABLE_DEBUG=1
    export DJANGO_SETTINGS_MODULE=my_api.settings.local
    export DJANGO_SECRET_KEY=MyVerySecretKey
    export DJANGO_SUPERUSER_USERNAME=superuser
    export DJANGO_SUPERUSER_PASSWORD=password
    export DJANGO_SUPERUSER_EMAIL=superuser@domain.local

Build and run with docker-compose::

    docker-compose -f docker-compose.drf_ms_pg.yml up --force-recreate
    docker-compose -f docker-compose.drf_ms_pg.yml exec -u postgres db1_pg psql -c 'CREATE DATABASE drfms_db;'
    docker-compose -f docker-compose.drf_ms_pg.yml exec -T -u postgres db1_pg psql drfms_db < db_pg_initiate.sql
    docker-compose -f docker-compose.drf_ms_pg.yml exec drf_ms_pg python manage.py migrate --noinput
    docker-compose -f docker-compose.drf_ms_pg.yml exec drf_ms_pg python manage.py collectstatic --noinput
    docker-compose -f docker-compose.drf_ms_pg.yml exec drf_ms_pg python manage.py createsuperuser --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --noinput
    docker-compose -f docker-compose.drf_ms_pg.yml down

Now everything is fine, you can run it as service::

    docker-compose -f docker-compose.drf_ms_pg.yml up -d

Or Close and clean, remove All of the compose file, with permanents volume also::

    docker-compose -f docker-compose.drf_ms_pg.yml down -v --rmi local --remove-orphans
    or with also downloaded images
    docker-compose -f docker-compose.drf_ms_pg.yml down -v --rmi all --remove-orphans

Or Close and clean, remove All of the compose file, except permanents volume (to save your data for future use)::

    docker-compose -f docker-compose.drf_ms_pg.yml down --rmi local --remove-orphans
    or with also downloaded images
    docker-compose -f docker-compose.drf_ms_pg.yml down --rmi all --remove-orphans

usefull cmds::

    docker exec -it drf-microservice_db1_pg_1 psql -d drfms_db -U drfms_user


.. include:: links.inc

Usage
========
+ Now we just jump in the new directory and run tox to ::
    - be sure that everything as worked fine
    - generate the documentation
    - generate an virtualenv


run tests::

    cd drf-microservice
    tox

+ An virtualenv is already ready for you at ::

    tox -l
    py38-django31

+ or you can create your ::

    python3 -m venv /pass/to/venv

+ Activate it ::

    source .tox/py38-django31/bin/activate

+ Then ::

    SECRET_KEY=my_secret_key python manage.py makemigrations
    SECRET_KEY=my_secret_key python manage.py migrate
    SECRET_KEY=my_secret_key python manage.py createsuperuser

- if you want enable the debug mode ::

    ENABLE_DEBUG=1

nut if you don't you need to deploy the static files::

    python manage.py collectstatic

- then run it ::

    SECRET_KEY=my_secret_key python manage.py runserver

- the existing endpoints in production are::

    /swagger/openapi(?P<format>\.json|\.yaml)
    /swagger/openapi/
    /swagger/redoc/
    /admin/
    /api-auth/
    /api-auth-token/
    /docs/
    /icinga/
    /icinga2/
    /api/v1/file/
    /media/(?P<path>.*)
    /400/
    /403/
    /404/
    /500/
    /media/(?P<path>.*)

- added endpoints for tests are::

    ^swagger/openapi(?P<format>\.json|\.yaml)$ [name='schema-json-or-yaml']
    ^swagger/openapi/$ [name='schema-openapi-ui']
    ^swagger/redoc/$ [name='schema-redoc']
    admin/
    ^api-auth/
    ^api-auth-token/$ [name='get_auth_token']
    ^docs/
    icinga/ [name='icinga']
    icinga2/ [name='icinga2']
    api/v1/file [name='api_file']
    ^media/(?P<path>.*)$
    ^400/$ [name='handler400']
    ^403/$ [name='handler403']
    ^404/$ [name='handler404']
    ^500/$ [name='handler500']
    ^media/(?P<path>.*)$

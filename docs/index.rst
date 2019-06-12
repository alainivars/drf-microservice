Welcome to drf-microservice cookiecutter's documentation!
=========================================================

.. image:: https://api.travis-ci.org/alainivars/drf-microservice.svg?branch=master
    :target: http://travis-ci.org/alainivars/drf-microservice
    :alt: Build status

.. image:: https://coveralls.io/repos/github/alainivars/drf-microservice/badge.svg?branch=master
    :target: https://coveralls.io/github/alainivars/drf-microservice?branch=master
    :alt: Test coverage status

.. image:: https://requires.io/github/alainivars/drf-microservice/requirements.svg?branch=master
    :target: https://requires.io/github/alainivars/drf-microservice/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://img.shields.io/pypi/dm/drf-microservice.svg
   :target: https://pypi.python.org/pypi/drf-microservice/
   :alt: pypi download

.. image:: https://img.shields.io/pypi/pyversions/drf-microservice.svg
   :target: https://pypi.python.org/pypi/drf-microservice/
   :alt: python supported

.. image:: https://img.shields.io/pypi/l/drf-microservice.svg
   :target: https://pypi.python.org/pypi/drf-microservice/
   :alt: licence

.. image:: https://img.shields.io/pypi/v/drf-microservice.svg
   :target: https://pypi.python.org/pypi/drf-microservice
   :alt: PyPi version

.. image:: https://landscape.io/github/alainivars/drf-microservice/master/landscape.svg?style=flat
   :target: https://landscape.io/github/alainivars/drf-microservice/master
   :alt: Code Health

.. image:: https://readthedocs.org/projects/drf-microservice/badge/?version=latest
   :target: https://readthedocs.org/projects/drf-microservice/?badge=latest
   :alt: Documentation status

.. image:: https://pypip.in/wheel/drf-microservice/badge.svg
   :target: https://pypi.python.org/pypi/drf-microservice/
   :alt: PyPi wheel



About drf-microservice Cookiescutter
====================================
drf-microservice is a ready-to-use API skeleton, Cookiescutter generates it, add your endpoints, test it, package it, validate it on stage and deploy it.
It sounds simple and it is. 
Something disturb you in the code? Don't hesitate to submit a pull request and contribute.

Releases Notes
==============
    - 0.6.1: Update dependencies
    - 0.6.0: total refactoring for add cookiecutter
    - 0.5.2: fix depencies security alert
    - 0.5.1: fix some document presentation on github and pypi
    - 0.5.0: Initial publication version

To setup
========
+ If needed install https://github.com/audreyr/cookiecutter or ::

    pip install cookiecutter


+ Cookiescutter will generate it for you ::

    cookiecutter gh:alainivars/drf-microservice                                                                                                                    00:31:00
    github_username [my-github-user-name]: alainivars
    github_repository_name [my-repository]: my-drf-microservice
    app_name [my_app]: my_api
    email [my-email@my-domain.my]: alainivars@gmail.com
    description [The description of my drf app]: A simple demo on how to use drf-microservice generator

+ Now we just jump in the new directory and run tox to ::

    - be sure that everything as worked fine
    - generate the documentation
    - generate an virtualenv


    cd my-drf-microservice
    tox

+ An virtualenv is already ready for you at ::

    tox -l
    py36-django222

+ or you can create your ::

    python3 -m venv /pass/to/venv

+ for bash, zsh ::

    source .tox/py36-django222/bin/activate

+ for fish ::

    source .tox/py36-django222/bin/activate.fish

+ for bash, zsh ::

    SECRET_KEY=my_secret_key
    python setup.py makemigration
    python manage.py migrate
    python manage.py createsuperuser

- for fish ::

    env SECRET_KEY=my_secret_key
    python setup.py makemigration
    python manage.py migrate
    python manage.py createsuperuser

- then run it ::

    SECRET_KEY=my_secret_key
    python manage.py runserver

- if you have any problem or you want enable the debug mode ::

    ENABLE_DEBUG=1


API
===
To see the documentation for the API
In development mode, login at ::

    curl --request POST \
      --url http://127.0.0.1:8000/rest-auth/login/ \
      --header 'authorization: Basic YWRtaW46YWRtaW4=' \
      --header 'content-type: application/json' \
    }'

Actually the default mode is "development" (same to the state of this project)
in that mode a default login is the the db with username='admin' password='admin'
you will get back in return your token.
 
Then open ::

    http://127.0.0.1:8000/docs/

Testing
=======
You can run the tests by ::

    SECRET_KEY=my_secret_key python manage.py test

or by ::

    python setup.py test

or by ::

    DJANGO_SETTINGS_MODULE={{cookiecutter.app_name}}.config.local SECRET_KEY=my_secret_key pytest


Security check
==============
Before dockerization for deployment to production, don't forget to check if by ::

    SECRET_KEY=my_secret_key python manage.py check --deploy


If you Use Aws
==============
Aws secret required ???::

    APPNAME_USERNAME_PASSWD => a client API password
    SECRET_KEY => the secret key

Aws Env required::

    AWS_REGION_NAME => default="eu-east-1"
    AWS_APPNAME_SECRET_NAME =>The name of the secret bucket

Build and run the image with Docker
===================================

Build the Docker image::

    docker build -t my-drf -f Dockerfile.drf-microservice .
    docker build -t my-nginx -f Dockerfile.nginx .

Run the container::

    docker network create my-network
    docker run -d --name drf --net my-network -v /app my-drf
    docker run -d --name nginx --net my-network -p "5000:80" my-nginx

If you want to change the port binding, it's here...


Build and run wit docker-compose::

    docker-compose up


Functionalities DONE
====================
    - support basic auth
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken
    - postgreSQL support

DevOps tools DONE
=================
    - the docker-image configuration file
    - the docker-compose configuration file
    - endpoint get status Icinga2

Functionalities TODO
====================
    - AWS ssm secret
    - endpoint json file DELETE,PUT?
    - create differents version:
        - Aws S3 support (in progress)
        - Aws RDS support
        - Aws Elastisearch support
        - Redis support
        - Aerospike support
        - ... 

DevOps tools TODO
=================
    - the Packer configuration file  (in progress)
    - the Terraform configuration file AWS (in progress)
    - the Terraform configuration file GCD
    - the Terraform configuration file Azure
    - add getSentry support
    - add Aws Cloudwatch support
    - the Ansible configuration file AWS
    - the Ansible configuration file GCD
    - the Ansible configuration file Azure
    - the Juju configuration file AWS
    - the Juju configuration file GCD
    - the Juju configuration file Azure


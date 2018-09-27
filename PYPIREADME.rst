.. image:: https://api.travis-ci.org/alainivars/drf-microservice.svg?branch=master
   :target: http://travis-ci.org/alainivars/drf-microservice
   :alt: Build status

.. image:: https://coveralls.io/repos/alainivars/drf-microservice/badge.svg?branch=devel
   :target: https://coveralls.io/r/alainivars/drf-microservice?branch=devel
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



Releases Notes
==============

    - 0.5.1: fix some document presentation on github and pypi
    - 0.5.0: Initial publication version

Requirements
============

    - Python 3.5, 3.6
    - Django 2.1.1

Features
========

* Functionalities::

A POC of a DRF microservice

!!!DON"T USE IT IN PRODUCTION, It's in development!!!

Something disturb you in the code? Don't hesitate to submit a pull request and contribute.

    - support basic auth
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken

Todo
====

    - AWS ssm secret
    - add getSentry support
    - endpoint json file DELETE,PUT?
    - add some strong auth
    - create differents version:
        - S3
        - RDS
        - postgreSQL
        - Redis
        - Aerospike
        - ...

for different use-case
======================

    - create the docker-image file
    - create the ansible file
    - create the terraform file
    - create the kubertes file
    - create the Juju file


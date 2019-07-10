
.. include:: links.inc

Functionalities
===============
    - support basic auth
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken
    - endpoint get status and running version
    - postgreSQL support
    - doc Swagger-OpenApi v2:
        this exposes 4 new endpoints:
            A JSON view of your API specification at /swagger/openapi.json
            A YAML view of your API specification at /swagger/openapi.yaml
            A swagger-ui view of your API specification at /swagger/openapi/
            A ReDoc view of your API specification at /swagger/redoc/
        - `API validation badge`_
        - `Code generation`_ with `Swagger codeGen`_
        And soo much more, take a look at:
        https://github.com/axnsan12/drf-yasg

Todo
----
    - AWS ssm secret
    - endpoint json file DELETE,PUT?
    - create different version:
        - Aws S3 support (in progress)
        - Aws RDS support
        - Aws Elastisearch support
        - Redis support
        - Aerospike support
        - ...


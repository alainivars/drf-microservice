CREATE DATABASE drfms_db;

CREATE USER drfms_user WITH ENCRYPTED PASSWORD 'drfms_pass';
ALTER ROLE drfms_user SET client_encoding TO 'utf8';
ALTER ROLE drfms_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE drfms_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE drfms_db TO drfms_user;

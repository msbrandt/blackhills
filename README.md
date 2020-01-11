# blackhills
Creating network "blackhills_postgres_conn" with driver "bridge"
Creating volume "blackhills_blackhills" with default driver
Building postgres
Step 1/14 : FROM postgres:11
 ---> 9fafa44ec2b0
Step 2/14 : ENV POSTGISV 2.5
 ---> Using cache
 ---> 8a8c44aa58ea
Step 3/14 : ENV TZ America/Denver
 ---> Using cache
 ---> 78b850a6f86e
Step 4/14 : RUN mkdir -p /opt/apps
 ---> Using cache
 ---> 1b05e476bc63
Step 5/14 : COPY ./pgsql-address-dictionary.zip /opt/apps/pgsql-address-dictionary.zip
 ---> Using cache
 ---> 2c0046c72738
Step 6/14 : RUN apt-get update
 ---> Using cache
 ---> e8bb98f3b189
Step 7/14 : RUN apt-get install -y --no-install-recommends   postgresql-$PG_MAJOR-postgis-$POSTGISV   postgresql-$PG_MAJOR-postgis-$POSTGISV-scripts   postgresql-$PG_MAJOR-pgrouting   postgresql-$PG_MAJOR-pgrouting-scripts   postgresql-server-dev-$PG_MAJOR   unzip   make   && cd /opt/apps   && unzip pgsql-address-dictionary.zip   && cd pgsql-addressing-dictionary-master   && make install   && apt-get purge -y --auto-remove postgresql-server-dev-$PG_MAJOR make unzip
 ---> Running in 40c0077e997b
Reading package lists...
Building dependency tree...
Reading state information...
E: Unable to locate package postgresql-11-postgis-2.5
E: Couldn't find any package by glob 'postgresql-11-postgis-2.5'
E: Couldn't find any package by regex 'postgresql-11-postgis-2.5'
E: Unable to locate package postgresql-11-postgis-2.5-scripts
E: Couldn't find any package by glob 'postgresql-11-postgis-2.5-scripts'
E: Couldn't find any package by regex 'postgresql-11-postgis-2.5-scripts'
E: Unable to locate package postgresql-11-pgrouting
E: Unable to locate package postgresql-11-pgrouting-scripts
E: Unable to locate package postgresql-server-dev-11
ERROR: Service 'postgres' failed to build: The command '/bin/sh -c apt-get install -y --no-install-recommends   postgresql-$PG_MAJOR-postgis-$POSTGISV   postgresql-$PG_MAJOR-postgis-$POSTGISV-scripts   postgresql-$PG_MAJOR-pgrouting   postgresql-$PG_MAJOR-pgrouting-scripts   postgresql-server-dev-$PG_MAJOR   unzip   make   && cd /opt/apps   && unzip pgsql-address-dictionary.zip   && cd pgsql-addressing-dictionary-master   && make install   && apt-get purge -y --auto-remove postgresql-server-dev-$PG_MAJOR make unzip' returned a non-zero code: 100


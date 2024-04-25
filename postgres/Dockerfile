FROM postgres:16.2

ADD ./init/* /docker-entrypoint-initdb.d/

RUN chmod a+r /docker-entrypoint-initdb.d/*

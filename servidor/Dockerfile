FROM ubuntu
MAINTAINER mexcel zapata "mexcel.zapata@mail.udp.cl"
MAINTAINER nicolas corra "nicolas.correa2@mail.udp.cl"
WORKDIR /taller 
ARG BEBIAN_FRONTED=noninteractive
RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get install -y build-essential \ 
&& apt-get install -y make 
RUN apt-get install nano \
&& apt install -y gcc zlib1g-dev libreadline6-dev \
&& apt-get -y install wget 
#RUN cd /usr/local/src 
RUN wget https://ftp.postgresql.org/pub/source/v13.0/postgresql-13.0.tar.bz2 
RUN tar -xvf postgresql-13.0.tar.bz2 
RUN cd postgresql-13.0 
RUN mkdir /opt/PostgreSQL-13/ 
WORKDIR /taller/postgresql-13.0/
RUN ./configure --prefix=/opt/PostgreSQL-13 
RUN make
RUN make install 
ENV PASS='12345'
#RUN mount -o remount,rw /
RUN useradd postgres
RUN passwd postgres
RUN echo $PASS > New password:
RUN echo $PASS > Retype new password:
RUN mkdir -p /pgdatabase/data
RUN chown -R postgres. /pgdatabase/data
RUN echo 'export PATH=$PATH:/opt/PostgreSQL-13/bin' > /etc/profile.d/postgres.sh
WORKDIR /taller/postgresql-13.0/src/bin/
#RUN chmod +x initdb
RUN chown -R postgres:root /taller/postgresql-13.0/src/bin/
RUN su postgres
RUN export PATH=$PATH:/taller/postgresql-13.0/src/bin/
#RUN /taller/postgresql-13.0/src/bin/initdb -D /pgdatabase/data -U postgres -W
RUN /taller/postgresql-13.0/src/bin/initdb -D /pgdatabase/data/ -U postgres -W
#RUN initdb -D /pgdatabase/data/ -U postgres -W
ENV PASS=123
RUN echo $PASS > Enter new superuser password:
RUN echo $PASS > Enter it again: 
RUN pg_ctl -D /pgdatabase/data/ -l logfile start
RUN psql -p 5432
RUN CREATE DATABASE taller WITH OWNER postgres;
RUN create table usuarios ( nombre varchar(30), clave varchar(10));
RUN insert into usuarios (nombre, clave) values ('nico', 'meme');
EXPOSE 80/tcp


FROM ubuntu
MAINTAINER mexcel zapata "mexcel.zapata@mail.udp.cl"
MAINTAINER nicolas corra "nicolas.correa2@mail.udp.cl"

ARG BEBIAN_FRONTED=noninteractive

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y install postgresql-client 

EXPOSE 5432/tcp
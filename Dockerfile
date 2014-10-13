FROM stackbrew/debian:wheezy
MAINTAINER Mozilla Cloud Services

RUN echo "deb http://ftp.debian.org/debian sid main" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y python3-requests

ADD loadtest.py /loadtest.py
CMD python3.4 loadtest.py

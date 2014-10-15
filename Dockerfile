FROM stackbrew/debian:wheezy
MAINTAINER Mozilla Cloud Services

RUN echo "deb http://ftp.debian.org/debian sid main" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y python-requests
RUN apt-get install -y python-pip
RUN pip install influxdb

ADD loadtest.py /loadtest.py
CMD python loadtest.py

FROM ubuntu:14.04
MAINTAINER jonthdiaz <jonthdiaz@gmail.com>

#update packeges
RUN apt-get update

#install the packages of the system 
RUN apt-get install -qy python \
                        python3.4 \
                        python-dev \
                        python3-dev \
                        python-pip \
                        python-setuptools \
                        build-essential \
                        python3-pip \
                        libcurl4-openssl-dev \
                        libpq-dev

RUN apt-get install -qy vim \
                        wget \
                        net-tools \
                        git \
                        curl \
                        zsh \
                        git-core

#expose port 
EXPOSE 8080

#copy app
RUN mkdir /digital-works
WORKDIR /digital-works

ADD requirements.txt  /digital-works

ADD run_web.sh /digital-works
RUN chmod 755 run_web.sh

#alias 
RUN alias python=/usr/bin/python3.4

#install requirements
RUN pip3 install -r /digital-works/requirements.txt

#RUN pip3 freeze
#create unprivileged user
RUN adduser --disabled-password --gecos '' dw

#permisos para file run_web.sh
#RUN chmod +x manage.py
#RUN chmod +x run_web.sh
#CMD ['/bin/bash', '/run_web.sh']

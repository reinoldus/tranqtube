############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu/Debia
############################################################
FROM python:latest

MAINTAINER Stefan Hesse

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN useradd --create-home --shell /bin/bash flask && echo "flask:flask" | chpasswd && adduser flask sudo && passwd -d flask

EXPOSE 8000

USER flask

ENV PATH=$PATH:/home/flask/.local/bin

ADD /deploy-requirements.txt /home/flask/tranqtube/requirements.txt

RUN pip3 install --user -r /home/flask/tranqtube/requirements.txt

# Has to be here, otherwise app folder is root user?!
COPY /tranqtube /home/flask/tranqtube/tranqtube/
COPY /tranqtube/boot.py /home/flask/tranqtube/
COPY /settings.cfg /home/flask/tranqtube/

USER root

RUN chown flask:flask -R /home/flask/

USER flask

ENV FLASK_APP=tranqtube TRANQTUBE_SETTINGS=../settings.cfg

WORKDIR /home/flask/tranqtube

# CMD gunicorn -k 'eventlet' -b 0.0.0.0:8000 boot:app

CMD gunicorn -b 0.0.0.0:8000 boot:app
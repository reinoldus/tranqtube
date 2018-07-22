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

ADD /deploy-requirements.txt /home/flask/tranqtube/requirements.txt

RUN pip3 install -r /home/flask/tranqtube/requirements.txt && chown flask:flask -R /home/flask/

# Has to be here, otherwise app folder is root user?!
COPY /tranqtube /home/flask/tranqtube/tranqtube/
COPY /tranqtube/boot.py /home/flask/tranqtube/
COPY /settings.cfg /home/flask/tranqtube/

ENV FLASK_APP=tranqtube TRANQTUBE_SETTINGS=../settings.cfg

USER flask

WORKDIR /home/flask/tranqtube

# CMD gunicorn -k 'eventlet' -b 0.0.0.0:8000 boot:app

CMD gunicorn -b 0.0.0.0:8000 boot:app
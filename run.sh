#!/usr/bin/env bash

export FLASK_APP=tranqtube
export TRANQTUBE_SETTINGS=../settings.cfg

./venv/bin/flask run
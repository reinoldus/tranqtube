#!/usr/bin/env bash

export FLASK_APP=tranqtube
export TRANQTUBE_SETTINGS=../settings.cfg
export FLASK_DEBUG=True

./venv/bin/flask run
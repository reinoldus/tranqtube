#!/usr/bin/env bash

yarn install
cp -R ./node_modules/jquery/dist/ ./tranqtube/static/jquery
cp -R ./node_modules/video.js/dist/ ./tranqtube/static/video.js
rm -rf ./node_modules/
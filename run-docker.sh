#!/usr/bin/env bash

docker-compose pull
docker-compose build

docker-compose up -d
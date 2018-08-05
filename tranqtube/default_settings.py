import os

DEBUG = False  # make sure DEBUG is off unless enabled explicitly otherwise
LOG_DIR = '.'  # create log files in current working directory
MONGO = os.getenv("MONGO", 'mongodb://localhost:27017/') # Available Docker in docker compose network network
VIDEO_SERVER_IP = os.getenv("VIDEO_SERVER_IP", "http://localhost:4444")

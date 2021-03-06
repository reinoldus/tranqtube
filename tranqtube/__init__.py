import base64
import os
from flask import Flask

from tranqtube.misc import string_to_base64

app = Flask(__name__)
app.config.from_object('tranqtube.default_settings')
# app.config.from_envvar('MONGO', True)
# app.config.from_envvar('VIDEO_SERVER_IP', True)
#app.config.from_envvar('TRANQTUBE_SETTINGS')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'tranqtube.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)

import tranqtube.views




# populate bytes for jinja
app.jinja_env.globals.update(string_to_base64=string_to_base64)
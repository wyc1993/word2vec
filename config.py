import logging
FORMAT = '%(asctime)-15s %(message)s'
LOG_FILE = "log_file"
logging.basicConfig(format = FORMAT,filename = LOG_FILE)

info_logger = logging.getLogger("debug")
info_logger.setLevel(logging.DEBUG)
err_logger = logging.getLogger("error")
err_logger.setLevel(logging.ERROR)

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


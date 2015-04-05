# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('project')
app.config.from_object("config")
app.debug = True
#toolbar = DebugToolbarExtension(app)

from project.controllers import *

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


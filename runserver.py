#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app, db

from flask.ext.script import Server, Shell, Manager, prompt_bool
from project.models import Relation, Word

manager = Manager(app)

manager.add_command("runserver", Server('0.0.0.0',port=8008, threaded=True))

@manager.command
def createall():
    "Create all database tables"
    db.create_all()

    Word.add(Word("test"))
    Word.add(Word("hello"))

@manager.command
def dropall():
    "Drops all database tables"
    if prompt_bool("Are you sure ? You will lose all your data !"):
        db.drop_all()

@manager.command
def showall():
    print "--------------"
    print "word:"
    for w in Word.query:
        print w

    print "relation: "
    for r in Relation.query:
        print r

if __name__ == "__main__":
    manager.run()

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
    _session = db.session

    filename = app.config["INIT_DATA"]
    print filename
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = unicode(line, "utf-8")
        print line
        words = line.split(",")
        key_word = words[0]
        heat_degree = float(words[1])
        
        i = 2
        while i < len(words)-1:
            word = words[i]
            weight = float(words[i+1])
            _session.add(Relation(key_word, word, weight))
            i = i+2
        _session.add(Word(key_word, heat_degree, words[i]))
        
    _session.commit()

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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app, db

from flask.ext.script import Server, Shell, Manager, prompt_bool
from project.models import Relation, Word, Heat

import random

manager = Manager(app)

manager.add_command("runserver", Server('0.0.0.0',port=8008, threaded=True))

def create_heat(n, x):
    result = ""
    for i in xrange(1,n):
        result = result + str(round(random.uniform(0.5*x, min(1, 2*x)), 4)) + ","
    #result = result + str(round(random.uniform(0.5*x, 2*x), 4))
    result = result + str(round(x, 4))
    print result
    return result

def init_all_heats(wordlists, wordheat):
    _session = db.session
    for w in wordlists:
        h = 0
        if wordheat.has_key(w):
            h = wordheat[w]
        else:
            h = round(random.uniform(0.01, 0.1), 4)

        _session.add(Word(w, h))
        for i in xrange(0, 12):
            _session.add(Heat(w, round(random.uniform(0.5*h, min(0.99, 2*h)), 4), i ))
    _session.commit()

from crawler.baike import get_keywords
@manager.command
def createall():
    "Create all database tables"
    db.create_all()
    _session = db.session

    filename = app.config["INIT_DATA"]
    print filename
    with open(filename, 'r') as f:
        lines = f.readlines()

    wordlists = []
    wordheat = {}
    for line in lines:
        line = unicode(line, "utf-8")
        print line
        words = line.split(",")
        key_word = words[0]
        heat_degree = float(words[1])
        
        wordlists.append(key_word)
        wordheat[key_word] = heat_degree

        i = 2
        while i < len(words)-1:
            word = words[i]
            weight = float(words[i+1])
            _session.add(Relation(key_word, word, weight))
            i = i+2

            wordlists.append(word)

        #_session.add(Heat(key_word, create_heat(12, heat_degree)))
        #_session.add(Word(key_word, heat_degree, words[i]))
    _session.commit()

    wordlists = list(set(wordlists))
    init_all_heats(wordlists, wordheat)

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

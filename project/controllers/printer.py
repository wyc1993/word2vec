# -*- coding: utf-8 -*-
from project import app
from project.models import Relation

from flask import render_template, request
import json

@app.route('/')
def start():
    return render_template('index.html')

from project.models.Relation import get_relations

@app.route("/get_vec", methods=["post"])
def get_vec():
    para = request.get_json()
    word = para["word"]

    result = get_relations(word)
    print result
    return json.dumps(result)

from project.models.Word import get_top_heat
@app.route("/get_top_word", methods=["post"])
def get_top_word():
	result = get_top_heat(5)
	return json.dumps(result)

@app.route("/test", methods=["get"])
def test():
	return "hello world"
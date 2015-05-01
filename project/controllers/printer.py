# -*- coding: utf-8 -*-
from project import app
from project.models import Relation

from flask import render_template, request
import json

import os

@app.route('/')
def start():
    return render_template('index.html')

from project.models.Relation import get_relations

@app.route("/get_vec", methods=["post"])
def get_vec():
    para = request.get_json()
    word = para["word"]

    result = get_relations(word)
    return json.dumps(result)

from project.models.Word import get_top_heat
from project.models.Heat import get_top_hot_of_month
@app.route("/get_top_word", methods=["post"])
def get_top_word():
	para = request.get_json()
	month = 0
	if para.has_key("month"):
		month = para["month"]

	number = 5
	if para.has_key("number"):
		number = para["number"]

	result = get_top_hot_of_month(number, month)
	return json.dumps(result)

@app.route("/test", methods=["get"])
def test():
	return "hello world"

@app.route("/baike", methods=["get", "post"])
def baike():
	word = request.get_json()["word"]
	filename = app.config["BAIKE_DIR"] + '/' + word;

	if os.path.exists(filename) == False:
		print "no such file, will get from baidu baike"

		from crawler.baike import get_keywords
		get_keywords(word, filename)

	result = open(filename).read()
	return result

@app.route("/get_heats", methods = ["post"])
def get_heats():
	word = request.get_json()["word"]
	
	from project.models.Heat import get_heats
	result = get_heats(word)

	return json.dumps(result)

@app.route("/past_hotword", methods = ["get", "post"])
def past_hotword():
	return render_template("past_hotword.html")

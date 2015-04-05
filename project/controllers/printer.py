# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
import json

@app.route('/')
def start():
    return render_template('index.html')


@app.route("/get_vec", methods=["post"])
def get_vec():
    para = request.get_json()
    print para
    word = para["word"]

    result = {"hehe": 0.8, "haha":0.7, "wangyici": 0.9, "lmx": 0.1, "cs": 0.3, "computer": 0.7, "movie": 0.3 }
    return json.dumps(result)


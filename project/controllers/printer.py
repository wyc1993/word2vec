# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
from flask.ext.wtf import Form, TextField, validators
import json

class CreateForm(Form):
    text = TextField(u'Text:', [validators.Length(min=1, max=20)])


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

@app.route('/print', methods=['GET', 'POST'])
def printer():
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        from project.models.Printer import Printer
        printer = Printer()
        printer.show_string(form.text.data)
        return render_template('printer/index.html')
    return render_template('printer/print.html', form=form)

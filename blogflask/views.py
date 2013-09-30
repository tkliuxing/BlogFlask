# -*- coding: utf-8 -*-
from blogflask import app
from flask.ext.mako import render_template


@app.route('/')
def hello_world():
    C = {}
    C['content'] = 'test'
    return render_template("index.html", **C)

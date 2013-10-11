# -*- coding: utf-8 -*-
from flask.ext.mako import render_template
from flask import request, abort
from blogflask import app
from blogflask.crypto import get_random_string


@app.route('/')
def hello_world():
    C = {}
    content = ur"""使用了Django-pygments组件使内容中的代码块高亮显示.

需要使用`<pre><code></code></pre>`标签把代码块包起来

效果如下:
<pre><code>
@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Gre\'ater'
    return (param2 - param1 + 1) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
</code></pre>
"""
    # C['text'] = mkdown(content)
    C['text'] = content
    return render_template("index.html", **C)

@app.route('/add/', methods=['POST', 'GET'])
def create_blog():
    if request.method == 'GET':
        return render_template("edit.html")
    if request.method == 'POST':
        C = {
            'title': request.form.get('title', None),
            'content': request.form.get('content', None),
        }
        #print C, request.form.items()
        return render_template("edit.html", C=C)
    abort(404)
